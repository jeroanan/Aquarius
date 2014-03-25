import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.output.console.ConsoleStrings import ConsoleStrings
from aquarius.output.console.SearchScreen import SearchScreen


class TestSearchScreen(unittest.TestCase):

    def setUp(self):
        self.__initialise_app()
        self.__initialise_search_screen()
        self.__initialiseStringsMock()
        self.__search_screen.SetStringsObject(self.__strings)

    def __initialiseStringsMock(self):
        self.__strings = ConsoleStrings()
        self.__strings.get_search_result_title_string = Mock()
        self.__strings.get_search_result_footer_string = Mock()

    def __initialise_app(self):
        self.__app = Aquarius("hardcoded", None, None)
        self.__app.search_books = Mock(return_value=[Book()])

    def __initialise_search_screen(self):
        self.__search_screen = SearchScreen(self.__app)
        self.__search_screen.input = lambda: None

    def testMainDoesTheSearch(self):
        self.__search_screen.main()
        self.assertTrue(self.__strings.get_search_result_title_string.called)
        self.assertTrue(self.__strings.get_search_result_footer_string.called)
        self.assertTrue(self.__app.search_books.called)
