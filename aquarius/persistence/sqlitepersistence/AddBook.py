class AddBook(object):

    def __init__(self, parameter_sanitiser):
        self.__sanitiser = parameter_sanitiser

    def add_book(self, book, connection):
        book_id = self.__get_existing_book_id(book, connection)
        if book_id is None:
            book.id = self.__add_new_book_returning_its_id(book, connection)
        else:
            book.id = book_id
        self.__add_book_formats(book, connection)

    def __add_new_book_returning_its_id(self, book, conn):
        (title, author) = self.__sanitiser.sanitise((
            book.title, book.author))

        sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (title, author)
        conn.execute_sql(sql)
        return conn.get_last_row_id()

    def __get_existing_book_id(self, book, conn):
        (title, author) = self.__sanitiser.sanitise((
            book.title, book.author))
        sql = "SELECT Id FROM Book WHERE Title='%s' AND Author='%s'" % (title, author)
        r = list(conn.execute_sql_fetch_all(sql))
        if len(r) > 0:
            return r[0][0]

    def __add_book_formats(self, book, connection):
        for f in book.formats:
            self.add_format(book, connection, f)

    def add_format(self, book, connection, f):
        if not self.__format_exists(book, f, connection):
            self.__add_new_format(book, connection, f)

    def __format_exists(self, book, book_format, connection):
        (book_id, bf) = self.__sanitiser.sanitise((book.id, book_format.Format))
        sql = "SELECT 1 FROM BookFormat WHERE Book='%s' AND FORMAT='%s'" % (book_id, bf)
        return len(connection.execute_sql_fetch_all(sql)) > 0

    def __add_new_format(self, book, connection, f):
        (book_id, book_format, location) = \
            self.__sanitiser.sanitise((book.id, f.Format, f.Location))
        sql = "INSERT INTO BookFormat (Book, Format, Location) VALUES (%s, '%s', '%s')" % \
              (book_id, book_format, location)
        connection.execute_sql(sql)
