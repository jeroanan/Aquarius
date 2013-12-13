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
    
    
    
    
    
    
    
    
    
