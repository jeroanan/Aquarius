from aquarius.persistence.sqlitepersistence.connection import connection

class databasecreation(object):
    
    def __init__(self, config):
        self.__config  = config
        
    def CreateDb(self):
        sql = self.__GetContentsOfDatabaseScript()
        self.__executeSql(sql)
        
    def __executeSql(self, sql):
        with connection(self.__config) as conn:
            for statement in sql.split(";"):
                conn.ExecuteSql(statement)            
                    
    def __GetContentsOfDatabaseScript(self):
        with open("aquarius/persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch