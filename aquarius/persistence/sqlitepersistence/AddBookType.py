class AddBookType(object):

    def __init__(self, sanitiser):
        self.__parameter_sanitiser = sanitiser

    def add_book_type(self, book_type, connection):
        (f, mt) = self.__parameter_sanitiser.sanitise(
            (book_type.Format, book_type.MimeType))
        sql = "INSERT INTO FORMAT (Code, MimeType) VALUES ('%s', '%s')" % \
              (f, mt)
        connection.execute_sql(sql)
