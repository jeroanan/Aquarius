from aquarius.persistence.sqlitepersistence.connection import connection


class databasecreation(object):
    
    def __init__(self, config):
        self.__config  = config
        
    def CreateDb(self):
        sql = self.__get_contents_of_database_script()
        self.__execute_sql(sql)
        
    def __execute_sql(self, sql):
        with connection(self.__config) as conn:
            for statement in sql.split(";"):
                conn.ExecuteSql(statement)            
                    
    @staticmethod
    def __get_contents_of_database_script():
        with open("aquarius/persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch