import unittest

from aquarius.persistence.sqlitepersistence.GetBookDetails \
    import GetBookDetails
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy \
    import ParameterSanitiserSpy


class TestGetBookDetails(unittest.TestCase):

    def setUp(self):
        self.__conn = ConnectionSpy()
        self.__book_details = GetBookDetails()

    def testGetBookDetailsMakesCorrectCalls(self):
        self.__book_details.get_book_details(1, self.__conn)
        self.assertEquals(1, self.__conn.fetch_all_with_params_calls)