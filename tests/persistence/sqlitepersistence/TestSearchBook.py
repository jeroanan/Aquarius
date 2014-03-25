import unittest

from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from tests.persistence.sqlitepersistence.Mocks.ConnectionSpy import ConnectionSpy


class TestSearchBook(unittest.TestCase):

    def setUp(self):
        self.__search = SearchBook()
        self.__conn = ConnectionSpy()

    def test_search_books_calls_collaborating_objects_correctly(self):
        self.__doSearch("Treasure")
        self.assertEquals(2, self.__conn.fetch_all_with_params_calls)

    def __doSearch(self, search_term):
        return self.__search.search_books(search_term, self.__conn)
