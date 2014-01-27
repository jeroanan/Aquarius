from aquarius.objects.booktype import booktype
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class GetBookType(object):

    def __init__(self):
        self.__sanitiser = ParameterSanitiser()

    def get_book_type(self, format_code, connection):
        (f) = self.__sanitiser.sanitise((format_code,))
        sql = "SELECT Code, MimeType FROM Format WHERE Code='%s'" % list(f)[0]
        r = connection.execute_sql_fetch_all(sql)
        if len(r) > 0:
            bt = booktype()
            bt.Format = r[0][0]
            bt.MimeType = r[0][1]
            return bt

    def set_parameter_sanitiser(self, sanitiser):
        self.__sanitiser = sanitiser