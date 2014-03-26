class GetFormatsForBook(object):

    def __init__(self, connection):
        self.__connection = connection

    def execute(self, book):
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=?"
        formats = self.__connection.execute_sql_fetch_all_with_params(sql, (book.id,))
        return formats