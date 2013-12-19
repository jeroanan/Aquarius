from persistence.sqlitepersistence.addbook import addbook
from persistence.sqlitepersistence.connection import connection
from persistence.sqlitepersistence.databasecreation import databasecreation
from persistence.sqlitepersistence.searchbook import searchbook

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
