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
    
    def __BookExists(self, book):        
        titleResult = self.SearchBooks(book.Title)
        authorResult = self.SearchBooks(book.Author)
        return (book in titleResult or book in authorResult)       
        
    def SearchBooks(self, searchTerm):
        return self.__bookSearch.SearchBooks(searchTerm)
    
    def GetBookDetails(self, bookId):
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=%s" % bookId
        b = book()
        books = self.__convertSearchResultsToBooks(self.__connection.ExecuteSqlFetchAll(sql))
        if len(books)>0:
            b = books[0]
        return b
            
    def __convertSearchResultsToBooks(self, searchResult):
        books = []        
        for result in searchResult:            
            b = book()
            b.Id, b.Title, b.Author = result            
            books.append(b)
        return books
    