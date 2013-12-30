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
    
    
    
