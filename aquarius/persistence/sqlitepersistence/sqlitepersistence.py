from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat
from aquarius.objects.booktype import booktype
from aquarius.persistence.sqlitepersistence.addbook import addbook
from aquarius.persistence.sqlitepersistence.connection import connection
from aquarius.persistence.sqlitepersistence.databasecreation import databasecreation
from aquarius.persistence.sqlitepersistence.searchbook import searchbook


class sqlitepersistence(object):
    
    def GetInstance(self, config):
        return persistence(config, searchbook(), addbook())


class persistence(object):
    
    def __init__(self, config, bookSearch, bookAdd):
        self.__bookSearch = bookSearch
        self.__bookAdd = bookAdd
        self.__config = config
        databasecreation(config).CreateDb()
            
    def SearchBooks(self, searchTerm):
        with connection(self.__config) as conn:
            return self.__bookSearch.SearchBooks(searchTerm, conn)
    
    def GetBookDetails(self, bookId):
        with connection(self.__config) as conn:
            return self.__bookSearch.GetBookDetails(bookId, conn)      
    
    def AddBook(self, book):
        with connection(self.__config) as conn:
            self.__bookAdd.AddBook(book, conn)
    
    def AddBookType(self, booktype):
        sql = "INSERT INTO FORMAT (Code, MimeType) VALUES ('%s', '%s')" % (booktype.Format, booktype.MimeType)
        with connection(self.__config) as conn:
            conn.ExecuteSql(sql)
    
    def GetBookType(self, formatCode):        
        sql = "SELECT Code, MimeType FROM Format WHERE Code='%s'" % formatCode
        with connection(self.__config) as conn:
            r = conn.ExecuteSqlFetchAll(sql) 
        if len(r) > 0:       
            bt = booktype()
            bt.Format = r[0][0]
            bt.MimeType = r[0][1]
            return bt
   
    def ListBooksByFirstLetter(self, firstletter):
        sql = "SELECT b.Id, b.Title, b.Author FROM Book b WHERE Title LIKE '%s%s'" % (firstletter, "%")
        with connection(self.__config) as conn:
            return self.__convert_search_results_to_books(list(conn.ExecuteSqlFetchAll(sql)), conn)
        
    def __convert_search_results_to_books(self, searchResult, connection):
        books = []        
        for result in searchResult:            
            self.__convert_search_result_to_book(books, result, connection)
        return books
    
    def __convert_search_result_to_book(self, books, result, connection):
        b = book()
        b.Id, b.Title, b.Author = result        
        self.__add_formats_to_book(b, connection)
        books.append(b)
        
    def __add_formats_to_book(self, book, connection):
        formats = self.__get_formats_for_book(book, connection)
        for f in formats:
            self.__add_book_to_format(book, f)
    
    @staticmethod
    def __get_formats_for_book(book, connection):
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=%s" % book.Id
        formats = connection.ExecuteSqlFetchAll(sql)        
        return formats
    
    @staticmethod
    def __add_book_to_format(book, bookFormat):
        bf = bookformat()
        bf.Format, bf.Location = bookFormat
        book.Formats.append(bf)
