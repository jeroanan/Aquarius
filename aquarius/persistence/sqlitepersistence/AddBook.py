class AddBook(object):

    def __init__(self, connection):
        self.__connection = connection

    def execute(self, book):
        sql = "INSERT INTO Book (Title, Author) VALUES (?, ?)"
        self.__connection.execute_sql_with_params(sql, (book.title, book.author))
        return self.__connection.get_last_row_id()
