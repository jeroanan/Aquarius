from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter \
    import ListBooksByFirstLetter


class ListBooksByFirstLetterSpy(ListBooksByFirstLetter):

    def __init__(self):
        self.list_books_by_first_letter_calls = 0

    def list_books_by_first_letter(self, first_letter, conn):
        self.list_books_by_first_letter_calls += 1