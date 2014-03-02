import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.output.console.FirstLetterScreen import FirstLetterScreen
from aquarius.output.console.tests.ConsoleStringsMock import ConsoleStringsMock


class TestFirstLetterScreen(unittest.TestCase):

    def setUp(self):
        self.__a = Aquarius("hardcoded", None, None)
        self.__a.list_books_by_first_letter = Mock(return_value=[Book()])
        self.__f = FirstLetterScreen(self.__a)
        self.__strings = ConsoleStringsMock()
        self.__f.SetStringsObject(self.__strings)
        self.__f.input = lambda: None

    def testMainListsByFirstLetter(self):
        self.__f.main()
        self.AssertFirstLetterScreenRendered()

    def AssertFirstLetterScreenRendered(self):
        self.assertTrue(self.__strings.verify_printedfirstletterscreen())
        self.assertTrue(self.__a.list_books_by_first_letter.called)

