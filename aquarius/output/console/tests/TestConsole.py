import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.console.Console import Console
from aquarius.output.console.SearchScreen import SearchScreen
from aquarius.output.console.FirstLetterScreen import FirstLetterScreen


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.__inputKey = 0
        self.__alreadyInput = False
        self.__InitialiseMockApp()
        self.__InitialiseMockSearchScreen()
        self.__InitialiseMockFirstLetterScreen()
        self.__InitialiseConsole()

    def __InitialiseMockApp(self):
        self.__app = Aquarius("hardcoded", None, None)
        self.__app.harvest_books = Mock()

    def __InitialiseMockSearchScreen(self):
        self.__search_screen = SearchScreen(self.__app)
        self.__search_screen.input = self.__input
        self.__search_screen.main = Mock()

    def __InitialiseMockFirstLetterScreen(self):
        self.__first_letter_screen = FirstLetterScreen(self.__app)
        self.__first_letter_screen.input = self.__input
        self.__first_letter_screen.main = Mock()

    def __InitialiseConsole(self):
        self.__c = Console(self.__app, None)
        self.__c.set_search_screen(self.__search_screen)
        self.__c.set_first_letter_screen(self.__first_letter_screen)
        self.__c.input = self.__input

    def testPerformingSearchCallsSearchObject(self):
        self.__inputKey = "1"
        self.__c.main()
        self.assertTrue(self.__search_screen.main.called)

    def testListingByFirstLetterCallsFirstLetterObject(self):
        self.__inputKey = "2"
        self.__c.main()
        self.assertTrue(self.__first_letter_screen.main.called)

    def testDoingBookHarvestCallsAppObject(self):
        self.__inputKey = "3"
        self.__c.main()
        self.assertTrue(self.__app.harvest_books.called)

    def test_console_ignores_keyboard_interrupt(self):
        self.__app.harvest_books = Mock(side_effect=KeyboardInterrupt)
        self.__inputKey = "3"
        self.__c.main()

    def test_console_ignores_eof_error(self):
        self.__app.harvest_books = Mock(side_effect=EOFError)
        self.__inputKey = "3"
        self.__c.main()

    def __input(self):
        if not self.__alreadyInput:
            self.__alreadyInput = True
            return self.__inputKey
        else:
            return "0"



