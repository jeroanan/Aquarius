from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook


class SearchBookSpy(SearchBook):
    def __init__(self):
        self.search_books_calls = 0

    def search_books(self, search_term, connection):
        self.search_books_calls += 1