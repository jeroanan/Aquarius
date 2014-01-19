import os
import unittest

from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy \
    import ParameterSanitiserSpy


class TestSearchBook(unittest.TestCase):
    """Tests for the SearchBook class"""
    def setUp(self):
        """Common setup operations"""
        self.__search = SearchBook()
        self.__parameter_sanitiser = ParameterSanitiserSpy()
        self.__search.set_parameter_sanitiser(self.__parameter_sanitiser)
        self.__conn = ConnectionSpy()

    def testSearchBooksCallsCollaboratingObjectsCorrectly(self):
        """Given a boo search, then the book search calls its
        collaborating objects correctly"""
        self.__doSearch("Treasure")
        self.assertEquals(2, self.__conn.fetch_all_calls)
        self.assertEquals(2, self.__parameter_sanitiser.sanitise_calls)

    def __doSearch(self, search_term):
        return self.__search.search_books(search_term, self.__conn)

    def testGetBookDetailsCallsCollaboratingObjectsCorrectly(self):
        """Given a request for book details, then the book search calls its
        collaborating objects correctly"""
        self.__search.get_book_details(1, self.__conn)
        self.assertEquals(1, self.__parameter_sanitiser.sanitise_calls)
        self.assertEquals(1, self.__conn.fetch_all_calls)
