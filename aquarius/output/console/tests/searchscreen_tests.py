import unittest

from aquarius.aquarius import aquarius
from aquarius.output.console.consolestrings import consolestrings
from aquarius.output.console.searchscreen import searchscreen


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


class ConsoleStringsMock(consolestrings):

    def __init__(self):
        self.getsearchstringcalled = False
        self.getsearchresulttitlestringcalled = False
        self.getsearchresultfooterstringcalled = False

    def verify_printedsearchresults(self):
        return self.getsearchstringcalled \
            and self.getsearchresulttitlestringcalled \
            and self.getsearchresultfooterstringcalled

    def GetSearchResultTitleString(self):
        self.getsearchresulttitlestringcalled = True
        return None

    def GetSearchResultFooterString(self, numberofresults):
        self.getsearchresultfooterstringcalled = True
        return None

    def GetSearchString(self):
        self.getsearchstringcalled = True
        return None


class AquariusDummy(aquarius):
    def __init__(self):
        super().__init__("hardcoded", None, None)
        self.searchbookscalled = False

    def SearchBooks(self, searchterm):
        self.searchbookscalled = True
        return []
