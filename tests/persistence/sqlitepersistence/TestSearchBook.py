import unittest

from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from tests.persistence.sqlitepersistence.Mocks.ConnectionSpy import ConnectionSpy


class TestSearchBook(unittest.TestCase):

    def setUp(self):
        self.__conn = ConnectionSpy()
        self.__target = SearchBook(self.__conn)

    def test_search_books_calls_collaborating_objects_correctly(self):
        self.__target.execute("Treasure")
        self.assertEquals(2, self.__conn.fetch_all_with_params_calls)

    def test_search_books_no_results_returns_empty_list(self):
        result = self.__target.execute("Treasure")
        self.assertEqual(result, [])