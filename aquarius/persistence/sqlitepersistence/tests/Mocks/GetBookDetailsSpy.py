from aquarius.persistence.sqlitepersistence.GetBookDetails \
    import GetBookDetails


class GetBookDetailsSpy(GetBookDetails):
    def __init__(self):
        self.get_book_details_calls = 0

    def get_book_details(self, book_id, connection):
        self.get_book_details_calls += 1