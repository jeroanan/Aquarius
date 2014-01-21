from aquarius.persistence.sqlitepersistence.AddBook import AddBook


class AddBookSpy(AddBook):
    def __init__(self):
        self.add_book_calls = 0

    def add_book(self, book, connection):
        self.add_book_calls += 1

    def add_format(self, book, connection, f):
        pass