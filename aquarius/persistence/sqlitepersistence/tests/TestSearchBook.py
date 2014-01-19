import os
import unittest

from Config import Config
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser
from aquarius.persistence.sqlitepersistence.SqlitePersistence \
    import Persistence
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
        self.__doSearch("Treasure")
        self.assertEquals(2, self.__conn.fetch_all_calls)
        self.assertEquals(2, self.__parameter_sanitiser.sanitise_calls)

    def __doSearch(self, search_term):
        return self.__search.search_books(search_term, self.__conn)
