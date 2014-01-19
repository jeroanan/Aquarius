from aquarius.persistence.sqlitepersistence.Connection import Connection


class ConnectionSpy(Connection):
    """Test double for the connection object"""

    def __init__(self):
        """Set initial object state"""
        self.fetch_all_calls = 0
        self.fetch_none_calls = 0
        self.get_last_row_id_calls = 0

    def execute_sql_fetch_all(self, sql):
        """spy on execute_sql_fetch_all"""
        self.fetch_all_calls += 1
        return []

    def execute_sql(self, sql):
        """spy on execute_sql"""
        self.fetch_none_calls += 1

    def get_last_row_id(self):
        """Spy on get_last_row_id"""
        self.get_last_row_id_calls += 1