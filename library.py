"""hm12_job2"""


class Book:
    def __init__(self, book_name, author, num_pages, isbn, is_reserve=False, is_get=False):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserve = is_reserve
        self.is_get = is_get

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

    def print_user_can_not(self, operation, book):
        print(f"{self.name} can not {operation} {book.book_name}")

    def reserve_book(self, book):
        if book.is_reserve:
            self.print_user_can_not("reserve", book)
        else:
            self.reserve_books.append(book)
            book.is_reserve = True

    def cancel_reserve(self, book):
        if book in self.reserve_books:
            self.reserve_books.remove(book)
            book.is_reserve = False
        else:
            self.print_user_can_not("cancel reserve", book)

    def get_book(self, book):
        if book.is_get:
            self.print_user_can_not("get", book)
        elif book.is_reserve and book not in self.reserve_books:
            self.print_user_can_not("get", book)
        else:
            self.get_books.append(book)
            book.is_get = True
            book.is_reserve = False

    def return_book(self, book):
        if book in self.get_books:
            self.get_books.remove(book)
            book.is_get = False
        else:
            self.print_user_can_not("return", book)


book01 = Book(book_name="The Hobbit", author="Books by J.R.R. Tolkien", num_pages=400, isbn="0006754023")
book02 = Book(book_name="The Fellowship of the Ring", author="Books by J.R.R. Tolkien", num_pages=500, isbn="0008264062")
book03 = Book(book_name="The Two Towers", author="Books by J.R.R. Tolkien", num_pages=550, isbn="0008264079")
book04 = Book(book_name="The Return of the King", author="Books by J.R.R. Tolkien", num_pages=600, isbn="0008264222")

vasya = Reader("Vasya")
petya = Reader("Petya")

vasya.reserve_book(book01)
vasya.reserve_book(book01)
vasya.cancel_reserve(book01)
petya.reserve_book(book01)
vasya.get_book(book01)
petya.get_book(book01)
vasya.return_book(book01)
petya.return_book(book01)
vasya.get_book(book01)
