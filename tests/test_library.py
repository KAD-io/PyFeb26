from logging import getLogger
import pytest
from source.library import Reader, Book


logger = getLogger(__name__)


@pytest.fixture
def book():
    return Book("The Hobbit",
                "Books by J.R.R. Tolkien",
                400,
                "0006754023")


@pytest.fixture
def reader_01():
    return Reader(name="reader_01")


@pytest.fixture
def reader_02():
    return Reader(name="reader_02")


def test_reserve_book(reader_01, book):
    """Positive test: book reservations"""
    logger.info("Running test: book reservations")
    reader_01.reserve_book(book)
    assert book.is_reserve is True
    assert book in reader_01.reserve_books
    logger.info("Completing test: book reservations")


def test_cancel_reserve_book(reader_01, book):
    """Positive test: cancellation of reservation"""
    logger.info("Running test: cancellation of reservation")
    reader_01.reserve_book(book)
    reader_01.cancel_reserve(book)
    assert book.is_reserve is False
    assert book not in reader_01.reserve_books
    logger.info("Completing test: cancellation of reservation")


def test_get_book(reader_01, book):
    """Positive test: getting free book without booking"""
    logger.info("Running test: getting free book without booking")
    reader_01.get_book(book)
    assert book.is_reserve is False
    assert book not in reader_01.reserve_books
    assert book.is_get is True
    assert book in reader_01.get_books
    logger.info("Completing test: getting free book without booking")


def test_get_reserved_book(reader_01, book):
    """Positive test: getting book to the reader who booked it"""
    logger.info("Running test: getting book to the reader who booked it")
    reader_01.reserve_book(book)
    reader_01.get_book(book)
    assert book.is_reserve is False
    assert book not in reader_01.reserve_books
    assert book.is_get is True
    assert book in reader_01.get_books
    logger.info("Completing test: getting book to the reader who booked it")


def test_return_book(reader_01, book):
    """Positive test: book return"""
    logger.info("Running test: book return")
    reader_01.get_book(book)
    reader_01.return_book(book)
    assert book.is_get is False
    assert book not in reader_01.get_books
    logger.info("Completing test: book return")


def test_saving_reservation(reader_01, reader_02, book):
    """Positive test: Saving reservation for another reader after returning the book"""
    logger.info("Running test: saving reservation")
    reader_01.get_book(book)
    reader_02.reserve_book(book)
    reader_01.return_book(book)
    assert book.is_reserve is True
    assert book in reader_02.reserve_books
    logger.info("Completing test: saving reservation")


def test_reserve_already_reserved_book(reader_01, reader_02, book):
    """Negative tests: It is not possible to book а book that has already been booked"""
    logger.info("Running test: reserve already reserved book")
    reader_01.reserve_book(book)
    reader_02.reserve_book(book)
    assert book in reader_01.reserve_books
    assert book not in reader_02.reserve_books
    logger.info("Completing test: reserve already reserved book")


def test_get_book_already_taken(reader_01, reader_02, book):
    """Negative tests: Reader cannot take book that is already in another reader possession"""
    logger.info("Running test: get book already taken")
    reader_01.get_book(book)
    reader_02.get_book(book)
    assert book in reader_01.get_books
    assert book not in reader_02.get_books
    logger.info("Completing test: get book already taken")


def test_get_reserved_book_by_stranger(reader_01, reader_02, book):
    """Negative tests: Reader is not allowed to take book booked by another reader"""
    logger.info("Running test: get reserved book by stranger")
    reader_01.reserve_book(book)
    reader_02.get_book(book)
    assert book.is_get is False
    assert book not in reader_02.get_books
    logger.info("Completing test: get reserved book by stranger")


def test_cancel_other_persons_reserve(reader_01, reader_02, book):
    """Negative tests: Reader cannot cancel another reader's booking"""
    logger.info("Running test: cancel other persons reserve")
    reader_01.reserve_book(book)
    reader_02.cancel_reserve(book)
    assert book.is_reserve is True
    assert book in reader_01.reserve_books
    logger.info("Completing test: cancel other persons reserve")


def test_return_not_taken_book(reader_01, book):
    """Negative tests: The reader cannot return a book that he did not take"""
    logger.info("Running test: return not taken book")
    reader_01.return_book(book)
    assert book.is_get is False
    logger.info("Completing test: return not taken book")
