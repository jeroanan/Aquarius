from aquarius.persistence.sqlitepersistence.GetBookType import GetBookType


class GetBookTypeSpy(GetBookType):

    def __init__(self):
        self.get_book_type_calls = 0

    def get_book_type(self, format_code, connection):
        self.get_book_type_calls += 1