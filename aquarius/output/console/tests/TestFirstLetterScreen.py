import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.output.console.ConsoleStrings import ConsoleStrings
from aquarius.output.console.FirstLetterScreen import FirstLetterScreen


class TestFirstLetterScreen(unittest.TestCase):
    def setUp(self):
        self.InitialiseMockApp()
        self.InitialiseStringMock()
        self.__f = FirstLetterScreen(self.__a)
        self.__f.SetStringsObject(self.__strings)
        self.__f.input = lambda: None

    def InitialiseMockApp(self):
        self.__a = Aquarius("hardcoded", None, None)
        self.__a.list_books_by_first_letter = Mock(return_value=[Book()])

    def InitialiseStringMock(self):
        self.__strings = ConsoleStrings()
        self.__strings.get_first_letter_string = Mock()
        self.__strings.get_search_result_title_string = Mock()
        self.__strings.get_search_result_footer_string = Mock()

    def testMainListsByFirstLetter(self):
        self.__f.main()
        self.__assert_first_letter_screen_rendered()

    def __assert_first_letter_screen_rendered(self):
        self.assertTrue(self.__strings.get_first_letter_string.called)
        self.assertTrue(self.__strings.get_search_result_title_string.called)
        self.assertTrue(self.__strings.get_search_result_footer_string.called)
        self.assertTrue(self.__a.list_books_by_first_letter.called)

