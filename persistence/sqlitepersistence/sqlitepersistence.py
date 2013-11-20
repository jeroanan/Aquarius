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
        
    def AddBook(self, book):
        sql = "INSERT INTO Book (Title) VALUES ('%s')" % book.Title        
        self.__executeSql(sql)
        
    def SearchBooks(self, searchTerm):
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")
        sql = "SELECT * FROM Book WHERE TITLE LIKE '%s';" % searchTerm
        r = self.__executeSqlFetchAll(sql)
        return r
    
    def __executeSql(self, sql):
        self.__executeSqlFetchAll(sql)
    
    def __executeSqlFetchAll(self, sql):
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()
        r = c.execute(sql).fetchall()
        conn.commit()
        conn.close()
        return r
        
    def __ExecuteDatabaseScript(self):
        batch = self.__GetContentsOfDatabaseScript()
        for statement in batch.split(";"):
            self.__executeSql(statement)
            
    def __GetContentsOfDatabaseScript(self):
        with open("persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch
    
    

    
    
    
    
    
    
    
    
