class FormatExists(object):

    def __init__(self, connection):
        self.__connection = connection

    def execute(self, book_id, book_format):
        sql = "SELECT 1 FROM BookFormat WHERE Book=? AND Format=?"
        return len(self.__connection.execute_sql_fetch_all_with_params(sql, (book_id, book_format))) > 0