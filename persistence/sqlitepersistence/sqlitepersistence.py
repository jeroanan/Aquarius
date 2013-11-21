import sqlite3

class sqlitepersistence(object):
    
    def __init__(self, config):
        self.__config = config
        self.__createdb()
        
    def __createdb(self):
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()                
        self.__ExecuteDatabaseScript()            
        conn.close()
        
    def __ExecuteDatabaseScript(self):
        batch = self.__GetContentsOfDatabaseScript()
        for statement in batch.split(";"):
            self.__executeSql(statement)
            
    def __GetContentsOfDatabaseScript(self):
        with open("persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch
    
    def AddBook(self, book):
        sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (book.Title, book.Author)        
        self.__executeSql(sql)
        
    def SearchBooks(self, searchTerm):
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")        
        searchResult = self.__searchByTitle(searchTerm)        
        self.__appendSearchResultIfAny(searchResult, self.__searchByAuthor(searchTerm))                
        return searchResult
    
    def __appendSearchResultIfAny(self, resultSet, searchResult):
        if len(searchResult)>0:
            resultSet.append(searchResult)
        return resultSet
    
    def __searchByTitle(self, searchTerm):
        sql = "SELECT * FROM Book WHERE Title LIKE '%s';" % searchTerm
        return self.__executeSqlFetchAll(sql)
    
    def __searchByAuthor(self, searchTerm):
        sql = "SELECT * FROM Book WHERE Author LIKE '%s';" % searchTerm                
        return self.__executeSqlFetchAll(sql)
    
    def __executeSql(self, sql):
        self.__executeSqlFetchAll(sql) 
    
    def __executeSqlFetchAll(self, sql):
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()
        r = c.execute(sql).fetchall()
        conn.commit()
        conn.close()
        return r

    
    
    
    
    
    
    
    
