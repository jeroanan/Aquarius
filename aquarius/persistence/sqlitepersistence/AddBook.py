class AddBook(object):

    def __init__(self, connection):
        self.__connection = connection

    def add_book(self, book):
        sql = "INSERT INTO Book (Title, Author) VALUES (?, ?)"
        self.__connection.execute_sql_with_params(sql, (book.title, book.author))
        return self.__connection.get_last_row_id()

    # def __add_book_formats(self, book):
    #     for f in book.formats:
    #         self.add_format(book, f)
    #
    # def add_format(self, book, f):
    #     if not self.__format_exists(book, f):
    #         self.__add_new_format(book, f)

