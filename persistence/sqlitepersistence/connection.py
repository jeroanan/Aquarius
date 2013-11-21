import sqlite3

class connection(object):    
    
    def __init__(self, config):
        self.__config = config
    
    def ExecuteSql(self, sql):
        self.ExecuteSqlFetchAll(sql)
    
    def ExecuteSqlFetchAll(self, sql):
        self.__OpenConnection()
        r = self.__cursor.execute(sql).fetchall()
        self.__CloseConnection()
        return r
    
    def __OpenConnection(self):
        self.__conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        self.__cursor = self.__conn.cursor()

    def __CloseConnection(self):
        self.__conn.commit()
        self.__conn.close()

