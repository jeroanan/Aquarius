import sqlite3


class Connection(object):
    """Manages the connection to the sqlite database.
    can be used within a context manager (e.g. with statement)"""
    def __init__(self, config):
        """Set initial object state"""
        self.__config = config
        self.__conn = None
        self.__cursor = None

    def __enter__(self):
        """Begin context manager"""
        self.open_connection()
        return self

    def open_connection(self):
        """Open connection to the sqlite database"""
        self.__conn = sqlite3.connect(self.__config.sqllite_database_path)
        self.__cursor = self.__conn.cursor()

    def __exit__(self, *args):
        """End context manager"""
        self.close_connection()

    def close_connection(self):
        """Close connection to the sqlite database"""
        self.__conn.commit()
        self.__conn.close()

    def execute_sql(self, sql):
        """Execute sql, not returning any result"""
        self.execute_sql_fetch_all(sql)
    
    def execute_sql_fetch_all(self, sql):
        """Execute sql, returning the result set"""
        return self.__cursor.execute(sql).fetchall()
        
    def get_last_row_id(self):
        """Get the identifier of the last row to be
        inserted into the database"""
        return self.__cursor.lastrowid

