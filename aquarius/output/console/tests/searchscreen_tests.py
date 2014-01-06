import unittest

from aquarius.output.console.tests.AquariusDummy import AquariusDummy
from aquarius.output.console.searchscreen import searchscreen
from aquarius.output.console.tests.ConsoleStringsMock import ConsoleStringsMock


class searchscreen_tests(unittest.TestCase):
    """Note: These tests were written after some of the code they test."""

    def testMainDoesTheSearch(self):
        self.__arrange()
        self.__searchscreen.Main()
        self.assertTrue(self.__strings.verify_printedsearchresults())
        self.assertTrue(self.__app.searchbookscalled)

    def __arrange(self):
        self.__app = AquariusDummy()
        self.__searchscreen = searchscreen(self.__app)
        self.__searchscreen.input = lambda: None
        self.__strings = ConsoleStringsMock()
        self.__searchscreen.SetStringsObject(self.__strings)



