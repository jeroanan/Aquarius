from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class searchbook(object):            
    
    def SearchBooks(self, searchTerm, connection):
        self.__connection = connection
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")        
        searchResult = self.__do_search(searchTerm)
        return self.__convert_search_results_to_books(searchResult)
    
    def __do_search(self, searchTerm):
        searchResult = self.__search_by_title(searchTerm)
        searchResult = self.__append_search_result(searchResult, self.__search_by_author(searchTerm))
        return searchResult
    
    def __search_by_title(self, searchTerm):
        sql = """SELECT b.Id, b.Title, b.Author
               FROM Book as b 
               WHERE Title LIKE '%s';""" % searchTerm
        return self.__connection.ExecuteSqlFetchAll(sql)
    
    def __search_by_author(self, searchTerm):
        sql = """SELECT b.Id, b.Title, b.Author 
                 FROM Book as b 
                 WHERE Author LIKE '%s';""" % searchTerm                
        return self.__connection.ExecuteSqlFetchAll(sql)

    def __append_search_result(self, resultSet, searchResult):
        newlist = []
        self.__populate_new_list_from_old(resultSet, newlist)
        self.__populate_new_list_from_old(searchResult, newlist)
        return newlist

    @staticmethod
    def __populate_new_list_from_old(old, new):
        for element in old:
            if element not in new:
                new.append(element)
                
    def GetBookDetails(self, bookId, connection):
        self.__connection = connection
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=%s" % bookId
        b = book()
        books = self.__convert_search_results_to_books(connection.ExecuteSqlFetchAll(sql))
        if len(books)>0:
            b = books[0]
        return b
    
    def __convert_search_results_to_books(self, searchResult):
        books = []        
        for result in searchResult:            
            self.__convert_search_result_to_book(books, result)
        return books
    
    def __convert_search_result_to_book(self, books, result):
        b = book()
        b.Id, b.Title, b.Author = result
        self.__add_formats_to_book(b)
        books.append(b)
        
    def __add_formats_to_book(self, book):
        formats = self.__get_formats_for_book(book)
        for f in formats:
            self.__add_book_to_format(book, f)
    
    @staticmethod
    def __add_book_to_format(book, bookFormat):
        bf = bookformat()
        bf.Format, bf.Location = bookFormat
        book.Formats.append(bf)
                    
    def __get_formats_for_book(self, book):
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=%s" % book.Id
        formats = self.__connection.ExecuteSqlFetchAll(sql)        
        return formats
