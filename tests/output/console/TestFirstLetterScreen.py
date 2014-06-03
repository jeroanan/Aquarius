from unittest.mock import Mock

from aquarius.objects.Book import Book
from aquarius.output.console.ConsoleStrings import ConsoleStrings
from aquarius.output.console.FirstLetterScreen import FirstLetterScreen
from tests.output.console.ConsoleTestBase import ConsoleTestBase


class TestFirstLetterScreen(ConsoleTestBase):
    def setUp(self):
        self.initialise_app_mock()
        self.initialise_string_mock()
        self.__f = FirstLetterScreen(self.app)
        self.__f.SetStringsObject(self.__strings)
        self.__f.input = lambda: None

    def initialise_app_mock(self):
        ConsoleTestBase.initialise_app_mock(self)
        self.app.list_books_by_first_letter = Mock(return_value=[Book()])

    def initialise_string_mock(self):
        self.__strings = ConsoleStrings()
        self.__strings.get_first_letter_string = Mock()
        self.__strings.get_search_result_title_string = Mock()
        self.__strings.get_search_result_footer_string = Mock()

    def test_main_lists_by_first_letter(self):
        self.__f.main()
        self.__assert_first_letter_screen_rendered()

    def __assert_first_letter_screen_rendered(self):
        self.assertTrue(self.__strings.get_first_letter_string.called)
        self.assertTrue(self.__strings.get_search_result_title_string.called)
        self.assertTrue(self.__strings.get_search_result_footer_string.called)
        self.assertTrue(self.app.list_books_by_first_letter.called)

