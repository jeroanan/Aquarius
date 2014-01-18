class AddBook(object):
    """Adds books to the database"""
    def add_book(self, book, connection):
        """Add a book to the database"""
        book_id = self.__get_existing_book_id(book, connection)

        if book_id is None:
            book.Id = self.__add_new_book_returning_its_id(book, connection)
        else:
            book.Id = book_id
        self.__add_book_formats(book, connection)

    @staticmethod
    def __add_new_book_returning_its_id(book, conn):
        sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (book.Title, book.Author)
        conn.execute_sql(sql)
        return conn.get_last_row_id()

    @staticmethod
    def __get_existing_book_id(book, conn):
        sql = "SELECT Id FROM Book WHERE Title='%s' AND Author='%s'" % (book.Title, book.Author)
        r = list(conn.execute_sql_fetch_all(sql))
        if len(r) > 0:
            return r[0][0]

    def __add_book_formats(self, book, connection):
        for f in book.Formats:
            if not self.__format_exists(book, f, connection):
                sql = "INSERT INTO BookFormat (Book, Format, Location) VALUES (%s, '%s', '%s')" \
                    % (book.Id, f.Format, f.Location)
                connection.execute_sql(sql)

    @staticmethod
    def __format_exists(book, book_format, connection):
        sql = "SELECT 1 FROM BookFormat WHERE Book='%s' AND FORMAT='%s'" % (book.Id, book_format)
        r = connection.execute_sql_fetch_all(sql)
        return len(r) > 0


