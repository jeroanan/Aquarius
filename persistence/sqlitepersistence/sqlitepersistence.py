from persistence.sqlitepersistence.connection import connection
from persistence.sqlitepersistence.databasecreation import databasecreation
from persistence.sqlitepersistence.searchbook import searchbook

class sqlitepersistence(object):
    
    def GetInstance(self, config):
        return persistence(config, searchbook())

class persistence(object):
    
    def __init__(self, config, bookSearch):
        self.__bookSearch = bookSearch
        self.__config = config
        databasecreation(config).CreateDb()            

    def AddBook(self, book):
        with connection(self.__config) as conn:
            if not(self.__BookExists(book)):            
                book.Id = self.__AddNewBookReturningItsId(book, conn)
            else:
                book.Id = self.__GetExistingBookId(book, conn)            
            self.__AddBookFormats(book, conn)   
    
    def __BookExists(self, book):        
        titleResult = self.SearchBooks(book.Title)
        authorResult = self.SearchBooks(book.Author)
        return (book in titleResult or book in authorResult)
    
    def __AddNewBookReturningItsId(self, book, conn):
        sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (book.Title, book.Author)
        conn.ExecuteSql(sql)
        return conn.GetLastRowId()
    
    def __GetExistingBookId(self, book, conn):
        sql = "SELECT Id FROM Book WHERE Title='%s' AND Author='%s'" % (book.Title, book.Author)
        r = list(conn.ExecuteSqlFetchAll(sql))
        if len(r) > 0:
            return r[0][0]
        
    def __AddBookFormats(self, book, connection):
        for f in book.Formats:            
            if not self.__FormatExists(book, f, connection):
                sql = "INSERT INTO BookFormat (Book, Format) VALUES (%s, '%s')" % (book.Id, f)                    
                connection.ExecuteSql(sql)
    
    def __FormatExists(self, book, bookFormat, connection):
        sql = "SELECT 1 FROM BookFormat WHERE Book='%s' AND FORMAT='%s'" % (book.Id, bookFormat)
        r = connection.ExecuteSqlFetchAll(sql)
        return len(r)>0
    
    def SearchBooks(self, searchTerm):
        with connection(self.__config) as conn:
            return self.__bookSearch.SearchBooks(searchTerm, conn)
    
    def GetBookDetails(self, bookId):
        return self.__bookSearch.GetBookDetails(bookId)       
    
    