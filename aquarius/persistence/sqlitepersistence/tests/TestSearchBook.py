import unittest

from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy \
    import ParameterSanitiserSpy


class TestSearchBook(unittest.TestCase):

    def setUp(self):
        self.__parameter_sanitiser = ParameterSanitiserSpy()
        self.__search = SearchBook(self.__parameter_sanitiser)
        self.__conn = ConnectionSpy()

    def testSearchBooksCallsCollaboratingObjectsCorrectly(self):
        self.__doSearch("Treasure")
        self.assertEquals(2, self.__conn.fetch_all_calls)
        self.assertEquals(2, self.__parameter_sanitiser.sanitise_calls)

    def __doSearch(self, search_term):
        return self.__search.search_books(search_term, self.__conn)
