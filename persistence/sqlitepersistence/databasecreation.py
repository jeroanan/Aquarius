class databasecreation(object):
    
    def __init__(self, connection):
        self.__connection = connection
    
    def CreateDb(self):
        batch = self.__GetContentsOfDatabaseScript()
        for statement in batch.split(";"):
            self.__connection.ExecuteSql(statement)            
                    
    def __GetContentsOfDatabaseScript(self):
        with open("persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch