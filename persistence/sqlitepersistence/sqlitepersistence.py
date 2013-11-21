from persistence.sqlitepersistence.connection import connection

class sqlitepersistence(object):
    
    def __init__(self, config):
        self.__connection = connection(config)
        self.__createdb()
        
    def __createdb(self):
        batch = self.__GetContentsOfDatabaseScript()
        for statement in batch.split(";"):
            self.__connection.ExecuteSql(statement)            
                    
    def __GetContentsOfDatabaseScript(self):
        with open("persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch
    
    def AddBook(self, book):
        sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (book.Title, book.Author)        
        self.__connection.ExecuteSql(sql)
        
    def SearchBooks(self, searchTerm):
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")        
        searchResult = self.__searchByTitle(searchTerm)        
        self.__appendSearchResultIfAny(searchResult, self.__searchByAuthor(searchTerm))                
        return searchResult
    
    def __searchByTitle(self, searchTerm):
        sql = "SELECT * FROM Book WHERE Title LIKE '%s';" % searchTerm
        return self.__connection.ExecuteSqlFetchAll(sql)
    
    def __searchByAuthor(self, searchTerm):
        sql = "SELECT * FROM Book WHERE Author LIKE '%s';" % searchTerm                
        return self.__connection.ExecuteSqlFetchAll(sql)
    
    def __appendSearchResultIfAny(self, resultSet, searchResult):
        if len(searchResult)>0:
            resultSet.append(searchResult)
        return resultSet  
    
    
    
    
    
    
    
    
    
