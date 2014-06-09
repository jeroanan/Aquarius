class AddBookType(object):

    def __init__(self, connection):
        self.__connection = connection

    def execute(self, book_type):
        sql = "INSERT INTO FORMAT (Code, MimeType) VALUES (?, ?)"
        self.__connection.execute_sql_with_params(sql, (book_type.Format, book_type.MimeType))
