from aquarius.objects.BookType import BookType


class GetBookType(object):

    def get_book_type(self, format_code, connection):
        sql = "SELECT Code, MimeType FROM Format WHERE Code=?"
        r = connection.execute_sql_fetch_all_with_params(sql, (format_code,))
        if len(r) > 0:
            bt = BookType()
            bt.Format = r[0][0]
            bt.MimeType = r[0][1]
            return bt