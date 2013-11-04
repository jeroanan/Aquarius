import sqlite3

class sqlitepersistence(object):
    
    def __init__(self, config):
        self.__config = config
        self.__createdb()
    
    def __createdb(self):
        conn = sqlite3.connect(self.__config.SqlLiteDatabasePath)
        c = conn.cursor()
        
        with open("persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        
        for statement in batch.split(";"):
            c.execute(statement)
            
        conn.close()