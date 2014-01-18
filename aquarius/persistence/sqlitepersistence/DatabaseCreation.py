from aquarius.persistence.sqlitepersistence.Connection import Connection


class DatabaseCreation(object):
    """Creates the sqlite database schema"""
    def __init__(self, config):
        """Set initial object state"""
        self.__config = config
        
    def create_db(self):
        """Perform the database connection"""
        sql = self.__get_contents_of_database_script()
        self.__execute_database_creation_script(sql)
        
    def __execute_database_creation_script(self, sql):
        """Execute the database creation script"""
        with Connection(self.__config) as conn:
            for statement in sql.split(";"):
                conn.execute_sql(statement)
                    
    @staticmethod
    def __get_contents_of_database_script():
        """Read the contents of the database creation script into memory"""
        with open("aquarius/persistence/sqlitepersistence/createdb.sql") as f:
            batch = f.read()
        return batch