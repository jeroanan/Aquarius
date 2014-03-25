class GetExistingBookId(object):

    def __init__(self, connection):
        self.__connection = connection

    def get_existing_book_id(self, book):
        sql = "SELECT Id FROM Book WHERE Title=? AND Author=?"
        r = list(self.__connection.execute_sql_fetch_all_with_params(sql, (book.title, book.author)))
        if len(r) > 0:
            return r[0][0]
        return -1