import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.output.console.SearchScreen import SearchScreen
from aquarius.output.console.tests.ConsoleStringsMock import ConsoleStringsMock


class TestSearchScreen(unittest.TestCase):

    def setUp(self):
        self.__initialise_app()
        self.__initialise_search_screen()
        self.__strings = ConsoleStringsMock()
        self.__search_screen.SetStringsObject(self.__strings)

    def __initialise_app(self):
        self.__app = Aquarius("hardcoded", None, None)
        self.__app.search_books = Mock(return_value=[Book()])

    def __initialise_search_screen(self):
        self.__search_screen = SearchScreen(self.__app)
        self.__search_screen.input = lambda: None

    def testMainDoesTheSearch(self):
        self.__search_screen.main()
        self.assertTrue(self.__strings.verify_printedsearchresults())
        self.assertTrue(self.__app.search_books.called)
