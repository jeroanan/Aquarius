from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class SearchBook(object):
    """Handles search requests for the sqlite persistor"""

    def __init__(self):
        """Set initial object state"""
        self.__connection = None

    def search_books(self, search_term, connection):
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
        sql = """SELECT b.Id, b.Title, b.Author
               FROM Book as b 
               WHERE Title LIKE '%s';""" % search_term
        return self.__connection.ExecuteSqlFetchAll(sql)
    
    def __search_by_author(self, search_term):
        sql = """SELECT b.Id, b.Title, b.Author 
                 FROM Book as b 
                 WHERE Author LIKE '%s';""" % search_term
        return self.__connection.ExecuteSqlFetchAll(sql)

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
                
    def get_book_details(self, book_id, connection):
        self.__connection = connection
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=%s" % book_id
        b = book()
        books = self.__convert_search_results_to_books(connection.ExecuteSqlFetchAll(sql))
        if len(books)>0:
            b = books[0]
        return b
    
    def __convert_search_results_to_books(self, search_result):
        books = []        
        for result in search_result:
            self.__convert_search_result_to_book(books, result)
        return books
    
    def __convert_search_result_to_book(self, books, result):
        b = book()
        b.Id, b.Title, b.Author = result
        self.__add_formats_to_book(b)
        books.append(b)
        
    def __add_formats_to_book(self, a_book):
        formats = self.__get_formats_for_book(a_book)
        for f in formats:
            self.__add_book_to_format(a_book, f)
    
    @staticmethod
    def __add_book_to_format(a_book, book_format):
        bf = bookformat()
        bf.Format, bf.Location = book_format
        a_book.Formats.append(bf)
                    
    def __get_formats_for_book(self, book):
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=%s" % book.Id
        formats = self.__connection.ExecuteSqlFetchAll(sql)        
        return formats
