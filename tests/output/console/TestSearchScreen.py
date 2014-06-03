from unittest.mock import Mock

from aquarius.objects.Book import Book
from aquarius.output.console.ConsoleStrings import ConsoleStrings
from aquarius.output.console.SearchScreen import SearchScreen
from tests.output.console.ConsoleTestBase import ConsoleTestBase


class TestSearchScreen(ConsoleTestBase):

    def setUp(self):
        self.initialise_app_mock()
        self.__initialise_search_screen()
        self.__initialise_strings_mock()
        self.__search_screen.SetStringsObject(self.__strings)

    def initialise_app_mock(self):
        ConsoleTestBase.initialise_app_mock(self)
        self.app.search_books = Mock(return_value=[Book()])

    def __initialise_strings_mock(self):
        self.__strings = ConsoleStrings()
        self.__strings.get_search_result_title_string = Mock()
        self.__strings.get_search_result_footer_string = Mock()

    def __initialise_search_screen(self):
        self.__search_screen = SearchScreen(self.app)
        self.__search_screen.input = lambda: None

    def test_main_does_search(self):
        self.__search_screen.main()
        self.assert_called(self.__strings.get_search_result_title_string)
        self.assert_called(self.__strings.get_search_result_footer_string)
        self.assert_called(self.app.search_books)
