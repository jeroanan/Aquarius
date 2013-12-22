class addbook(object):
    
    def AddBook(self, book, connection):
        bookId = self.__GetExistingBookId(book, connection)
            
        if bookId == None:            
            book.Id = self.__AddNewBookReturningItsId(book, connection)
        else:
            book.Id = bookId            
        self.__AddBookFormats(book, connection)
    
    def __AddNewBookReturningItsId(self, book, conn):
        sql = "INSERT INTO Book (Title, Author) VALUES ('%s', '%s')" % (book.Title, book.Author)
        conn.ExecuteSql(sql)
        return conn.GetLastRowId()
    
    def __GetExistingBookId(self, book, conn):
        sql = "SELECT Id FROM Book WHERE Title='%s' AND Author='%s'" % (book.Title, book.Author)
        r = list(conn.ExecuteSqlFetchAll(sql))
        if len(r) > 0:
            return r[0][0]
        
    def __AddBookFormats(self, book, connection):
        for f in book.Formats:            
            if not self.__FormatExists(book, f, connection):
                sql = "INSERT INTO BookFormat (Book, Format, Location) VALUES (%s, '%s', '%s')" \
                    % (book.Id, f.Format, f.Location)                    
                connection.ExecuteSql(sql)
    
    def __FormatExists(self, book, bookFormat, connection):
        sql = "SELECT 1 FROM BookFormat WHERE Book='%s' AND FORMAT='%s'" % (book.Id, bookFormat)
        r = connection.ExecuteSqlFetchAll(sql)
        return len(r)>0


