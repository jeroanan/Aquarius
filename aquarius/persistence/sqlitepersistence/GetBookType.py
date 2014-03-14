from aquarius.objects.BookType import BookType


class GetBookType(object):

    def __init__(self, parameter_sanitiser):
        self.__sanitiser = parameter_sanitiser

    def get_book_type(self, format_code, connection):
        (f) = self.__sanitiser.sanitise((format_code,))
        sql = "SELECT Code, MimeType FROM Format WHERE Code='%s'" % list(f)[0]
        r = connection.execute_sql_fetch_all(sql)
        if len(r) > 0:
            bt = BookType()
            bt.Format = r[0][0]
            bt.MimeType = r[0][1]
            return bt