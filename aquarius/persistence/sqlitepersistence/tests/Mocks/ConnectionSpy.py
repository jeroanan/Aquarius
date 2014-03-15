from aquarius.persistence.sqlitepersistence.Connection import Connection


class ConnectionSpy(Connection):

    def __init__(self):
        self.fetch_all_calls = 0
        self.fetch_all_with_params_calls = 0
        self.fetch_none_calls = 0
        self.get_last_row_id_calls = 0

    def execute_sql_fetch_all(self, sql):
        self.fetch_all_calls += 1
        return []

    def execute_sql_fetch_all_with_params(self, sql, params):
        self.fetch_all_with_params_calls += 1
        return []

    def execute_sql(self, sql):
        self.fetch_none_calls += 1

    def get_last_row_id(self):
        self.get_last_row_id_calls += 1