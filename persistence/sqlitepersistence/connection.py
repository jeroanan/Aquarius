import sqlite3

class connection(object):    
    """Manages the connection to the sqlite database.
    MUST be used within a context manager (e.g. with statement)"""
    
    def __enter__(self):
        self.__OpenConnection()
        return self
    
    def __OpenConnection(self):
        self.__conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        self.__cursor = self.__conn.cursor()
        
    def __exit__(self, *args):
        self.__CloseConnection()
    
    def __CloseConnection(self):
        self.__conn.commit()
        self.__conn.close()
        
    def __init__(self, config):
        self.__config = config   
        
    def ExecuteSql(self, sql):
        self.ExecuteSqlFetchAll(sql)
    
    def ExecuteSqlFetchAll(self, sql):
        r = self.__cursor.execute(sql).fetchall()
        return r
        
    def GetLastRowId(self):
        return self.__cursor.lastrowid
    
    

