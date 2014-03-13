from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class BookFinder(object):

    def __init__(self):
        self.sanitiser = ParameterSanitiser()
        self.__connection = None

    def convert_search_results_to_books(self, search_result):
        books = []
        for result in search_result:
            self.__convert_search_result_to_book(books, result)
        return books

    def __convert_search_result_to_book(self, books, result):
        b = Book()
        b.id, b.title, b.author = result
        self.__add_formats_to_book(b)
        books.append(b)

    def __add_formats_to_book(self, a_book):
        formats = self.__get_formats_for_book(a_book)
        for f in formats:
            self.__add_book_to_format(a_book, f)

    def __get_formats_for_book(self, b):
        (i,) = self.sanitiser.sanitise((b.id,))
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=%s" % i
        formats = self.connection.execute_sql_fetch_all(sql)
        return formats

    @staticmethod
    def __add_book_to_format(a_book, book_format):
        bf = BookFormat()
        bf.Format, bf.Location = book_format
        a_book.formats.append(bf)

    def set_parameter_sanitiser(self, sanitiser):
        self.sanitiser = sanitiser