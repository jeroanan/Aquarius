import sqlite3

class sqlitepersistence(object):
    
    def __init__(self, config):
        self.__config = config
        self.__createdb()
        
    def __createdb(self):
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()        
        
        sql = self.GetContentsOfDatabaseScript()        
        self.ExecuteContentsOfDatabaseScript(c, sql)
            
        conn.close()
        
    def AddBook(self):
        pass
    
    def GetContentsOfDatabaseScript(self):
        with open("persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch
    
    def ExecuteContentsOfDatabaseScript(self, c, batch):
        for statement in batch.split(";"):
            c.execute(statement)