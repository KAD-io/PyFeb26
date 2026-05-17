from logging import getLogger
from unittest.mock import Mock
import random
import pytest

logger = getLogger(__name__)


@pytest.fixture
def stub_book_data():
    return {
        "book_name": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "num_pages": 400,
        "isbn": "0006754023"
    }


@pytest.fixture
def mock_book(stub_book_data):
    book = Mock()
    book.book_name = stub_book_data["book_name"]
    book.author = stub_book_data["author"]
    book.num_pages = stub_book_data["num_pages"]
    book.isbn = stub_book_data["isbn"]

    book.is_reserve = False
    book.is_get = False
    return book


class FakeReader:

    def __init__(self, name):
        self.name = name
        self.reserve_books = []
        self.get_books = []

    def reserve_book(self, book):
        if book.is_reserve:
            return
        self.reserve_books.append(book)
        book.is_reserve = True

    def cancel_reserve(self, book):
        if book in self.reserve_books:
            self.reserve_books.remove(book)
            book.is_reserve = False

    def get_book(self, book):
        if book.is_get or (book.is_reserve and book not in self.reserve_books):
            return
        self.get_books.append(book)
        book.is_get = True
        if book in self.reserve_books:
            self.cancel_reserve(book)

    def return_book(self, book):
        if book in self.get_books:
            self.get_books.remove(book)
            book.is_get = False


@pytest.fixture
def fake_reader_01():
    return FakeReader(name="reader_01")


@pytest.fixture
def fake_reader_02():
    return FakeReader(name="reader_02")


def test_reserve_book(fake_reader_01, mock_book):
    """Positive test: book reservations"""
    logger.info("Running test: book reservations")

    fake_reader_01.reserve_book(mock_book)

    assert mock_book.is_reserve is True
    assert mock_book in fake_reader_01.reserve_books
    logger.info("Completing test: book reservations")


def test_cancel_reserve_book(fake_reader_01, mock_book):
    """Positive test: cancellation of reservation"""
    logger.info("Running test: cancellation of reservation")

    fake_reader_01.reserve_book(mock_book)
    fake_reader_01.cancel_reserve(mock_book)

    assert mock_book.is_reserve is False
    assert mock_book not in fake_reader_01.reserve_books
    logger.info("Completing test: cancellation of reservation")


def test_get_book(fake_reader_01, mock_book):
    """Positive test: getting free book without booking"""
    logger.info("Running test: getting free book without booking")

    fake_reader_01.get_book(mock_book)

    assert mock_book.is_reserve is False
    assert mock_book.is_get is True
    assert mock_book in fake_reader_01.get_books
    logger.info("Completing test: getting free book without booking")


def test_get_reserved_book(fake_reader_01, mock_book):
    """Positive test: getting book to the reader who booked it"""
    logger.info("Running test: getting book to the reader who booked it")

    fake_reader_01.reserve_book(mock_book)
    fake_reader_01.get_book(mock_book)

    assert mock_book.is_reserve is False
    assert mock_book.is_get is True
    assert mock_book in fake_reader_01.get_books
    logger.info("Completing test: getting book to the reader who booked it")


def test_return_book(fake_reader_01, mock_book):
    """Positive test: book return"""
    logger.info("Running test: book return")

    fake_reader_01.get_book(mock_book)
    fake_reader_01.return_book(mock_book)

    assert mock_book.is_get is False
    assert mock_book not in fake_reader_01.get_books
    logger.info("Completing test: book return")


def test_saving_reservation(fake_reader_01, fake_reader_02, mock_book):
    """Positive test: Saving reservation for another reader after returning the book"""
    logger.info("Running test: saving reservation")

    fake_reader_01.get_book(mock_book)
    fake_reader_02.reserve_book(mock_book)
    fake_reader_01.return_book(mock_book)

    assert mock_book.is_reserve is True
    assert mock_book in fake_reader_02.reserve_books
    logger.info("Completing test: saving reservation")


def test_reserve_already_reserved_book(fake_reader_01, fake_reader_02, mock_book):
    """Negative test: It is not possible to book а book that has already been booked"""
    logger.info("Running test: reserve already reserved book")

    fake_reader_01.reserve_book(mock_book)
    fake_reader_02.reserve_book(mock_book)

    assert mock_book in fake_reader_01.reserve_books
    assert mock_book not in fake_reader_02.reserve_books
    logger.info("Completing test: reserve already reserved book")


def test_get_book_already_taken(fake_reader_01, fake_reader_02, mock_book):
    """Negative test: Reader cannot take book that is already in another reader possession"""
    logger.info("Running test: get book already taken")

    fake_reader_01.get_book(mock_book)
    fake_reader_02.get_book(mock_book)

    assert mock_book in fake_reader_01.get_books
    assert mock_book not in fake_reader_02.get_books
    logger.info("Completing test: get book already taken")


def test_get_reserved_book_by_stranger(fake_reader_01, fake_reader_02, mock_book):
    """Negative test: Reader is not allowed to take book booked by another reader"""
    logger.info("Running test: get reserved book by stranger")

    fake_reader_01.reserve_book(mock_book)
    fake_reader_02.get_book(mock_book)

    assert mock_book.is_get is False
    assert mock_book not in fake_reader_02.get_books
    logger.info("Completing test: get reserved book by stranger")


def test_cancel_other_persons_reserve(fake_reader_01, fake_reader_02, mock_book):
    """Negative test: Reader cannot cancel another reader's booking"""
    logger.info("Running test: cancel other persons reserve")

    fake_reader_01.reserve_book(mock_book)
    fake_reader_02.cancel_reserve(mock_book)

    assert mock_book.is_reserve is True
    assert mock_book in fake_reader_01.reserve_books
    logger.info("Completing test: cancel other persons reserve")


@pytest.mark.flaky(reruns=2)
def test_return_not_taken_book_unstable(fake_reader_01, mock_book):
    """Flaky test: return not taken book unstable"""
    logger.info("Running test: return not taken book (unstable)")

    if random.choice([True, False]):
        logger.error("Simulated random error!")
        assert False, "Random flaky failure"

    fake_reader_01.return_book(mock_book)

    assert mock_book.is_get is False
    logger.info("Completing test: return not taken book (unstable)")
