class AddBook(object):

    def add_book(self, book, connection):
        book_id = self.__get_existing_book_id(book, connection)
        if book_id is None:
            book.id = self.__add_new_book_returning_its_id(book, connection)
        else:
            book.id = book_id
        self.__add_book_formats(book, connection)

    def __add_new_book_returning_its_id(self, book, conn):
        sql = "INSERT INTO Book (Title, Author) VALUES (?, ?)"
        conn.execute_sql_with_params(sql, (book.title, book.author))
        return conn.get_last_row_id()

    def __get_existing_book_id(self, book, conn):
        sql = "SELECT Id FROM Book WHERE Title=? AND Author=?"
        r = list(conn.execute_sql_fetch_all_with_params(sql, (book.title, book.author)))
        if len(r) > 0:
            return r[0][0]

    def __add_book_formats(self, book, connection):
        for f in book.formats:
            self.add_format(book, connection, f)

    def add_format(self, book, connection, f):
        if not self.__format_exists(book, f, connection):
            self.__add_new_format(book, connection, f)

    def __format_exists(self, book, book_format, connection):
        sql = "SELECT 1 FROM BookFormat WHERE Book=? AND Format=?"
        return len(connection.execute_sql_fetch_all_with_params(sql, (book.id, book_format.Format))) > 0

    def __add_new_format(self, book, connection, f):
        sql = "INSERT INTO BookFormat (Book, Format, Location) VALUES (?, ?, ?)"
        connection.execute_sql_with_params(sql, (book.id, f.Format, f.Location))
