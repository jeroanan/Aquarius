from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType


class AddBookTypeSpy(AddBookType):
    def __init__(self):
        self.add_book_type_calls = 0

    def add_book_type(self, book_type):
        self.add_book_type_calls += 1