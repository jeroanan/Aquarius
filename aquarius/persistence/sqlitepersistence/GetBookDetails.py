from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class GetBookDetails(object):
    def __init__(self):
        self.__connection = None
        self.__sanitiser = ParameterSanitiser()

    def get_book_details(self, book_id, connection):
        self.__connection = connection
        (i,) = self.__sanitiser.sanitise((book_id,))
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=%s" % i
        b = Book()
        books = self.__convert_search_results_to_books(connection.execute_sql_fetch_all(sql))
        if len(books) > 0:
            b = books[0]
        return b

    def __convert_search_results_to_books(self, search_result):
        books = []
        for result in search_result:
            self.__convert_search_result_to_book(books, result)
        return books

    def __convert_search_result_to_book(self, books, result):
        b = Book()
        b.id, b.title, b.author = result
        self.__add_formats_to_book(b)
        books.append(b)

    def set_parameter_sanitiser(self, sanitiser):
        self.__sanitiser = sanitiser