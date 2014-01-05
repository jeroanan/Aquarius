import unittest
from aquarius.aquarius import aquarius
from aquarius.output.console.consolestrings import consolestrings

from aquarius.output.console.searchscreen import searchscreen


class searchscreen_tests(unittest.TestCase):
    """Note: These tests were written after some of the code they test."""

    def testMainDoesTheSearch(self):
        a = AquariusDummy()
        s = searchscreen(a)
        s.input = lambda: None
        strings = ConsoleStringsMock()
        s.SetStringsObject(strings)
        s.Main()
        self.assertTrue(strings.printedsearchresults())
        self.assertTrue(a.searchbookscalled)


class ConsoleStringsMock(consolestrings):

    def __init__(self):
        self.getsearchstringcalled = False
        self.getsearchresulttitlestringcalled = False
        self.getsearchresultfooterstringcalled = False

    def printedsearchresults(self):
        return self.getsearchstringcalled \
            and self.getsearchresulttitlestringcalled \
            and self.getsearchresultfooterstringcalled

    def GetSearchResultTitleString(self):
        self.getsearchresulttitlestringcalled = True
        return None

    def GetMainMenu(self):
        return None

    def GetSearchResultFooterString(self, numberofresults):
        self.getsearchresultfooterstringcalled = True
        return None

    def GetFirstLetterString(self):
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
