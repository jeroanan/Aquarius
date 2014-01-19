from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class SearchBook(object):
    """Handles search requests for the sqlite persistor"""

    def __init__(self):
        """Set initial object state"""
        self.__connection = None
        self.__sanitiser = ParameterSanitiser()

    def search_books(self, search_term, connection):
        """Perform a search for the given search term"""
        self.__connection = connection
        search_term = "%s%s%s" % ("%", search_term, "%")
        search_result = self.__do_search(search_term)
        return self.__convert_search_results_to_books(search_result)
    
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

    # TODO: This belongs in a separate class. Inherit common
    # functions between this and search
    def get_book_details(self, book_id, connection):
        """Get details about a particular book"""
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
        """Sets this object's sql parameter sanitiser object on-the-fly"""
        self.__sanitiser = sanitiser
