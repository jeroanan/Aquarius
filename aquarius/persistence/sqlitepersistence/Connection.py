import sqlite3


class Connection(object):

    def __init__(self, config):
        """Set initial object state"""
        self.__config = config
        self.__conn = None
        self.__cursor = None

    def __enter__(self):
        self.open_connection()
        return self

    def open_connection(self):
        self.__conn = sqlite3.connect(self.__config.sqllite_database_path)
        self.__cursor = self.__conn.cursor()

    def __exit__(self, *args):
        self.close_connection()

    def close_connection(self):
        self.__conn.commit()
        self.__conn.close()

    def execute_sql(self, sql):
        self.execute_sql_fetch_all(sql)
    
    def execute_sql_fetch_all(self, sql):
        return self.__cursor.execute(sql).fetchall()

    def execute_sql_fetch_all_with_params(self, sql, params):
        return self.__cursor.execute(sql, params).fetchall()

    def get_last_row_id(self):
        return self.__cursor.lastrowid