import unittest

from aquarius.persistence.sqlitepersistence.GetBookType import GetBookType
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy \
    import ParameterSanitiserSpy


class TestGetBookType(unittest.TestCase):

    def setUp(self):
        self.__sanitiser = ParameterSanitiserSpy()
        self.__g = GetBookType(self.__sanitiser)
        self.__conn = ConnectionSpy()

    def testCallingGetBookTypeMakesCorrectCalls(self):
        self.__g.get_book_type("EPUB", self.__conn)
        self.assertEquals(1, self.__sanitiser.sanitise_calls)
        self.assertEquals(1, self.__conn.fetch_all_calls)