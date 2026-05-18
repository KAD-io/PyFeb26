from logging import getLogger


LOGGER = getLogger(__name__)


class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserve = False
        self.is_get = False

    def reserve(self):
        self.is_reserve = True

    def cancel_reserve(self):
        self.is_reserve = False

    def get_book(self):
        self.is_get = True

    def return_book(self):
        self.is_get = False


class Reader:
    def __init__(self, name):
        self.name = name
        self.reserve_books = []
        self.get_books = []

    def reserve_book(self, book):
        if book.is_reserve:
            LOGGER.error('Reader "%s" -> Book "%s"', self.name, book.book_name)
        else:
            self.reserve_books.append(book)
            book.is_reserve = True
            LOGGER.info('Reader "%s" -> Book "%s"', self.name, book.book_name)

    def cancel_reserve(self, book):
        if book in self.reserve_books:
            self.reserve_books.remove(book)
            book.is_reserve = False
            LOGGER.info('Reader "%s" -> Book "%s"', self.name, book.book_name)
        else:
            LOGGER.error('Reader "%s" -> Book "%s"', self.name, book.book_name)

    def get_book(self, book):
        if book.is_get:
            LOGGER.error('Reader "%s" -> Book "%s"', self.name, book.book_name)
        elif book.is_reserve and book not in self.reserve_books:
            LOGGER.error('Reader "%s" -> Book "%s"', self.name, book.book_name)
        else:
            self.get_books.append(book)
            book.is_get = True
            LOGGER.info('Reader "%s" -> Book "%s"', self.name, book.book_name)
            if book in self.reserve_books:
                self.cancel_reserve(book)

    def return_book(self, book):
        if book in self.get_books:
            self.get_books.remove(book)
            book.is_get = False
            LOGGER.info('Reader "%s" -> Book "%s"', self.name, book.book_name)
        else:
            LOGGER.error('Reader "%s" -> Book "%s"', self.name, book.book_name)
