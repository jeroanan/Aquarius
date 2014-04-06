class AddBookFormat(object):

    def __init__(self, connection):
        self.__connection = connection

    def execute(self, book_id, book_format):
        sql = "INSERT INTO BookFormat (Book, Format, Location) VALUES (?, ?, ?)"
        self.__connection.execute_sql_with_params(sql, (book_id, book_format.Format, book_format.Location))
