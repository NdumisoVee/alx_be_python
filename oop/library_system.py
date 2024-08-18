class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self._file_size = file_size

    @property
    def file_size(self):
        return self._file_size

    def __str__(self):
        return f"E{super().__str__()}, File Size: {self.file_size}KB"



class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    def __str__(self):
        return f"Print{super().__str__()}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        for book in self.books:
            print(book)
