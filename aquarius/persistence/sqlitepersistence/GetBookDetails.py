from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.BookFinder import BookFinder
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class GetBookDetails(BookFinder):
    def __init__(self):
        self.__connection = None
        self.__sanitiser = ParameterSanitiser()

    def get_book_details(self, book_id, connection):
        self.__connection = connection
        (i,) = self.__sanitiser.sanitise((book_id,))
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=%s" % i
        b = Book()
        books = self.convert_search_results_to_books(connection.execute_sql_fetch_all(sql))
        if len(books) > 0:
            b = books[0]
        return b

    def set_parameter_sanitiser(self, sanitiser):
        self.__sanitiser = sanitiser