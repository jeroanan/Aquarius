import unittest

from aquarius.persistence.sqlitepersistence.GetBookType import GetBookType
from tests.persistence.sqlitepersistence.Mocks.ConnectionSpy import ConnectionSpy


class TestGetBookType(unittest.TestCase):

    def setUp(self):
        self.__conn = ConnectionSpy()
        self.__g = GetBookType(self.__conn)

    def test_calling_get_book_type_makes_correct_calls(self):
        self.__g.get_book_type("EPUB")
        self.assertEquals(1, self.__conn.fetch_all_with_params_calls)