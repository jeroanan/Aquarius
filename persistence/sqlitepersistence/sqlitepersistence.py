import sqlite3

class sqlitepersistence(object):
    
    def __init__(self, config):
        self.__config = config
        self.__createdb()
        
    def __createdb(self):
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()        
        
        sql = self.__GetContentsOfDatabaseScript()        
        self.__ExecuteContentsOfDatabaseScript(c, sql)
            
        conn.close()
        
    def AddBook(self, book):
        sql = "INSERT INTO Book (Title) VALUES ('%s')" % book.Title        
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        conn.close()
        
    def SearchBooks(self, searchTerm):
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")
        sql = "SELECT * FROM Book WHERE TITLE LIKE '%s';" % searchTerm
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()
        r = c.execute(sql).fetchall()
        conn.close()
        return r
    
    def __GetContentsOfDatabaseScript(self):
        with open("persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch
    
    def __ExecuteContentsOfDatabaseScript(self, c, batch):
        for statement in batch.split(";"):
            c.execute(statement)

    
    
    
    
    
    
    
    
