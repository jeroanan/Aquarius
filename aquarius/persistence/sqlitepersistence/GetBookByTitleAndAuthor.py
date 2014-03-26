from aquarius.objects.Book import Book


class GetBookByTitleAndAuthor(object):

    def __init__(self, connection):
        self.__connection = connection

    def get_existing_book_id(self, book):
        b = Book()
        sql = "SELECT Id, Title, Author FROM Book WHERE Title=? AND Author=?"
        r = list(self.__connection.execute_sql_fetch_all_with_params(sql, (book.title, book.author)))
        if len(r) > 0:
            self.map_resultset_to_book(b, r)
        return b

    def map_resultset_to_book(self, book, resultset):
        book.id = resultset[0][0]
        book.title = resultset[0][1]
        book.author = resultset[0][2]
