import unittest

from aquarius.persistence.sqlitepersistence.GetBookDetails import GetBookDetails
from tests.persistence.sqlitepersistence.Mocks.ConnectionSpy import ConnectionSpy


class TestGetBookDetails(unittest.TestCase):

    def setUp(self):
        self.__conn = ConnectionSpy()
        self.__book_details = GetBookDetails(self.__conn)

    def test_get_book_details_makes_correct_Calls(self):
        self.__book_details.get_book_details(1)
        self.assertEquals(1, self.__conn.fetch_all_with_params_calls)