from unittest.mock import Mock

from aquarius.output.console.Console import Console
from aquarius.output.console.SearchScreen import SearchScreen
from aquarius.output.console.FirstLetterScreen import FirstLetterScreen
from tests.output.console.ConsoleTestBase import ConsoleTestBase


class TestConsole(ConsoleTestBase):

    def setUp(self):
        self.__inputKey = 0
        self.__alreadyInput = False
        self.initialise_app_mock()
        self.__initialise_mock_search_screen()
        self.__initialise_mock_first_letter_screen()
        self.__initialise_console()

    def initialise_app_mock(self):
        ConsoleTestBase.initialise_app_mock(self)
        self.app.harvest_books = Mock()

    def __initialise_mock_search_screen(self):
        self.__search_screen = SearchScreen(self.app)
        self.__search_screen.input = self.__input
        self.__search_screen.main = Mock()

    def __initialise_mock_first_letter_screen(self):
        self.__first_letter_screen = FirstLetterScreen(self.app)
        self.__first_letter_screen.input = self.__input
        self.__first_letter_screen.main = Mock()

    def __initialise_console(self):
        self.__c = Console(self.app, None)
        self.__c.set_search_screen(self.__search_screen)
        self.__c.set_first_letter_screen(self.__first_letter_screen)
        self.__c.input = self.__input

    def test_performing_search_calls_search_object(self):
        self.__inputKey = "1"
        self.__c.main()
        self.assert_called(self.__search_screen.main)

    def test_listing_by_first_letter_calls_first_letter_object(self):
        self.__inputKey = "2"
        self.__c.main()
        self.assert_called(self.__first_letter_screen.main)

    def test_doing_book_harvest_calls_app_object(self):
        self.__inputKey = "3"
        self.__c.main()
        self.assert_called(self.app.harvest_books)

    def test_console_ignores_keyboard_interrupt(self):
        self.app.harvest_books = Mock(side_effect=KeyboardInterrupt)
        self.__inputKey = "3"
        self.__c.main()

    def test_console_ignores_eof_error(self):
        self.app.harvest_books = Mock(side_effect=EOFError)
        self.__inputKey = "3"
        self.__c.main()

    def __input(self):
        if not self.__alreadyInput:
            self.__alreadyInput = True
            return self.__inputKey
        else:
            return "0"
