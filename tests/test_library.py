import unittest
from source.library import Reader, Book


class Testlibrary(unittest.TestCase):

    def setUp(self):
        self.book = Book("The Hobbit",
                         "Books by J.R.R. Tolkien",
                         400,
                         "0006754023")

        self.reader_01 = Reader("reader_01")
        self.reader_02 = Reader("reader_02")

    def test_reserve_book(self):
        """Positive test: book reservations"""
        self.reader_01.reserve_book(self.book)
        self.assertTrue(self.book.is_reserve)
        self.assertIn(self.book, self.reader_01.reserve_books)

    def test_cancel_reserve_book(self):
        """Positive test: cancellation of reservation"""
        self.reader_01.reserve_book(self.book)
        self.reader_01.cancel_reserve(self.book)
        self.assertFalse(self.book.is_reserve)
        self.assertNotIn(self.book, self.reader_01.reserve_books)

    def test_get_book(self):
        """Positive test: getting free book without booking"""
        self.reader_01.get_book(self.book)
        self.assertTrue(self.book.is_get)
        self.assertFalse(self.book.is_reserve)
        self.assertIn(self.book, self.reader_01.get_books)
        self.assertNotIn(self.book, self.reader_01.reserve_books)

    def test_get_reserved_book(self):
        """Positive test: getting book to the reader who booked it"""
        self.reader_01.reserve_book(self.book)
        self.reader_01.get_book(self.book)
        self.assertTrue(self.book.is_get)
        self.assertFalse(self.book.is_reserve)
        self.assertIn(self.book, self.reader_01.get_books)
        self.assertNotIn(self.book, self.reader_01.reserve_books)

    def test_return_book(self):
        """Positive test: book return"""
        self.reader_01.get_book(self.book)
        self.reader_01.return_book(self.book)
        self.assertFalse(self.book.is_get)
        self.assertNotIn(self.book, self.reader_01.get_books)
        self.assertNotIn(self.book, self.reader_01.reserve_books)

    def test_saving_reservation(self):
        """Positive test: Saving reservation for another reader after returning the book"""
        self.reader_01.get_book(self.book)
        self.reader_02.reserve_book(self.book)
        self.reader_01.return_book(self.book)
        self.assertNotIn(self.book, self.reader_01.reserve_books)
        self.assertTrue(self.book.is_reserve)
        self.assertIn(self.book, self.reader_02.reserve_books)

    def test_reserve_already_reserved_book(self):
        """Negative tests: It is not possible to book а book that has already been booked"""
        self.reader_01.reserve_book(self.book)
        self.reader_02.reserve_book(self.book)
        self.assertIn(self.book, self.reader_01.reserve_books)
        self.assertNotIn(self.book, self.reader_02.reserve_books)

    def test_get_book_already_taken(self):
        """Negative tests: Reader cannot take book that is already in another reader possession"""
        self.reader_01.get_book(self.book)
        self.reader_02.get_book(self.book)
        self.assertIn(self.book, self.reader_01.get_books)
        self.assertNotIn(self.book, self.reader_02.get_books)

    def test_get_reserved_book_by_stranger(self):
        """Negative tests: Reader is not allowed to take book booked by another reader"""
        self.reader_01.reserve_book(self.book)
        self.reader_02.get_book(self.book)
        self.assertFalse(self.book.is_get)
        self.assertNotIn(self.book, self.reader_02.get_books)

    def test_cancel_other_persons_reserve(self):
        """Negative tests: Reader cannot cancel another reader's booking"""
        self.reader_01.reserve_book(self.book)
        self.reader_02.cancel_reserve(self.book)
        self.assertTrue(self.book.is_reserve)
        self.assertIn(self.book, self.reader_01.reserve_books)

    def test_return_not_taken_book(self):
        """Negative tests: The reader cannot return a book that he did not take"""
        self.reader_01.return_book(self.book)
        self.assertFalse(self.book.is_get)
