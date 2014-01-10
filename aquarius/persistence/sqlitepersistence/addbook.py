class addbook(object):
    
    def AddBook(self, book, connection):
        bookId = self.__get_existing_book_id(book, connection)
            
        if bookId is None:
            book.Id = self.__add_new_book_returning_its_id(book, connection)
        else:
            book.Id = bookId            
        self.__add_book_formats(book, connection)
    
    @staticmethod
    def __add_new_book_returning_its_id(book, conn):
        sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (book.Title, book.Author)
        conn.ExecuteSql(sql)
        return conn.GetLastRowId()
    
    @staticmethod
    def __get_existing_book_id(book, conn):
        sql = "SELECT Id FROM Book WHERE Title='%s' AND Author='%s'" % (book.Title, book.Author)
        r = list(conn.ExecuteSqlFetchAll(sql))
        if len(r) > 0:
            return r[0][0]
        
    def __add_book_formats(self, book, connection):
        for f in book.Formats:            
            if not self.__format_exists(book, f, connection):
                sql = "INSERT INTO BookFormat (Book, Format, Location) VALUES (%s, '%s', '%s')" \
                    % (book.Id, f.Format, f.Location)                    
                connection.ExecuteSql(sql)
    
    @staticmethod
    def __format_exists(book, bookFormat, connection):
        sql = "SELECT 1 FROM BookFormat WHERE Book='%s' AND FORMAT='%s'" % (book.Id, bookFormat)
        r = connection.ExecuteSqlFetchAll(sql)
        return len(r)>0


