class AddBookType(object):

    def add_book_type(self, book_type, connection):
        sql = "INSERT INTO FORMAT (Code, MimeType) VALUES (?, ?)"
        connection.execute_sql_with_params(sql, (book_type.Format, book_type.MimeType))
