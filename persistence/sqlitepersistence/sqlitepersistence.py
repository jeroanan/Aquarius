from objects.book import book
from persistence.sqlitepersistence.connection import connection
from persistence.sqlitepersistence.databasecreation import databasecreation
from persistence.sqlitepersistence.searchbook import searchbook

class sqlitepersistence(object):
    
    def GetInstance(self, config):
        return persistence(config, searchbook(connection(config)))

class persistence(object):
    
    def __init__(self, config, bookSearch):
        self.__bookSearch = bookSearch
        self.__connection = connection(config)
        databasecreation(self.__connection).CreateDb()
        
    def AddBook(self, book):
        if not(self.__BookExists(book)):
            sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (book.Title, book.Author)        
            self.__connection.ExecuteSql(sql)
        self.__AddBookFormats(book)   
    
    def __BookExists(self, book):        
        titleResult = self.SearchBooks(book.Title)
        authorResult = self.SearchBooks(book.Author)
        return (book in titleResult or book in authorResult)
        
    def __AddBookFormats(self, book):
        for f in book.Formats:            
            if not(self.__FormatExists(book, f)):
                sql = "INSERT INTO BookFormat (Book, Format) VALUES (%s, '%s')" % (book.Id, f)
                self.__connection.ExecuteSql(sql)
    
    def __FormatExists(self, book, bookFormat):
        sql = "SELECT 1 FROM BookFormat WHERE Book='%s' AND FORMAT='%s'" % (book.Id, bookFormat)
        r = self.__connection.ExecuteSqlFetchAll(sql)
        return len(r)>0
    
    def SearchBooks(self, searchTerm):
        return self.__bookSearch.SearchBooks(searchTerm)
    
    def GetBookDetails(self, bookId):
        return self.__bookSearch.GetBookDetails(bookId)       
    
    