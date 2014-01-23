from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.BookFinder import BookFinder
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class SearchBook(BookFinder):

    def __init__(self):
        self.__connection = None
        self.__sanitiser = ParameterSanitiser()

    def search_books(self, search_term, connection):
        self.__connection = connection
        search_term = "%s%s%s" % ("%", search_term, "%")
        search_result = self.__do_search(search_term)
        return self.convert_search_results_to_books(search_result)
    
    def __do_search(self, search_term):
        search_result = self.__search_by_title(search_term)
        search_result = \
            self.__append_search_result(search_result,
                                        self.__search_by_author(search_term))
        return search_result
    
    def __search_by_title(self, search_term):
        (st) = self.__sanitiser.sanitise(search_term)
        sql = """SELECT b.Id, b.Title, b.Author
               FROM Book as b 
               WHERE Title LIKE '%s';""" % st
        return self.__connection.execute_sql_fetch_all(sql)
    
    def __append_search_result(self, result_set, search_result):
        new_list = []
        self.__populate_new_list_from_old(result_set, new_list)
        self.__populate_new_list_from_old(search_result, new_list)
        return new_list

    @staticmethod
    def __populate_new_list_from_old(old, new):
        for element in old:
            if element not in new:
                new.append(element)

    def __search_by_author(self, search_term):
        (st) = self.__sanitiser.sanitise(search_term)
        sql = """SELECT b.Id, b.Title, b.Author
                 FROM Book as b
                 WHERE Author LIKE '%s';""" % st
        return self.__connection.execute_sql_fetch_all(sql)
    
    def __add_formats_to_book(self, a_book):
        formats = self.__get_formats_for_book(a_book)
        for f in formats:
            self.__add_book_to_format(a_book, f)
    
    def __get_formats_for_book(self, b):
        (i,) = self.__sanitiser.sanitise((b.id,))
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=%s" % i
        formats = self.__connection.execute_sql_fetch_all(sql)
        return formats
                    
    @staticmethod
    def __add_book_to_format(a_book, book_format):
        bf = bookformat()
        bf.Format, bf.Location = book_format
        a_book.formats.append(bf)

    def set_parameter_sanitiser(self, sanitiser):
        self.__sanitiser = sanitiser
