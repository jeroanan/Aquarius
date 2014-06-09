from aquarius.objects.BookType import BookType


class GetBookType(object):

    def __init__(self, connection):
        self.__connection = connection

    def execute(self, format_code):
        sql = "SELECT Code, MimeType FROM Format WHERE Code=?"
        r = self.__connection.execute_sql_fetch_all_with_params(sql, (format_code,))
        if len(r) > 0:
            bt = BookType()
            bt.Format = r[0][0]
            bt.MimeType = r[0][1]
            return bt