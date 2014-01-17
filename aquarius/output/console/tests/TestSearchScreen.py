import unittest

from aquarius.output.console.tests.AquariusDummy import AquariusDummy
from aquarius.output.console.SearchScreen import SearchScreen
from aquarius.output.console.tests.ConsoleStringsMock import ConsoleStringsMock


class TestSearchScreen(unittest.TestCase):
    """Unit tests for the search screen"""
    def testMainDoesTheSearch(self):
        """Given a call to the search screen,
        then the search screen is rendered."""
        self.__arrange()
        self.__searchscreen.main()
        self.assertTrue(self.__strings.verify_printedsearchresults())
        self.assertTrue(self.__app.searchbookscalled)

    def __arrange(self):
        self.__app = AquariusDummy()
        self.__searchscreen = SearchScreen(self.__app)
        self.__searchscreen.input = lambda: None
        self.__strings = ConsoleStringsMock()
        self.__searchscreen.SetStringsObject(self.__strings)



