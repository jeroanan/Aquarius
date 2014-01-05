import unittest

from aquarius.output.console.console import console
from aquarius.output.console.firstletterscreen import firstletterscreen
from aquarius.output.console.searchscreen import searchscreen


class console_tests(unittest.TestCase):

    def setUp(self):
        self.__c = console(None, None)
        self.__inputKey = 0
        self.__alreadyInput = False

    def testMain(self):
        self.__c.input = lambda: "0"
        self.__c.Main()

    def testPerformingSearchCallsSearchObject(self):
        searchspy = SearchSpy()
        self.__c.SetSearchScreen(searchspy)
        self.__inputKey = "1"
        self.__c.input = self.__input
        self.__c.Main()
        self.assertTrue(searchspy.maincalled)

    def __input(self):
        if not self.__alreadyInput:
            self.__alreadyInput = True
            return self.__inputKey
        else:
            return "0"


class SearchSpy(searchscreen):

    def __init__(self):
        super().__init__(None)
        self.maincalled = False

    def Main(self):
        self.maincalled = True


class FirstLetterSpy(firstletterscreen):
     pass