import unittest

from aquarius.output.console.console import console

class console_tests(unittest.TestCase):

    def setUp(self):
        self.__inputKey = 0
        self.__alreadyInput = False
        self.__spy = Spy()
        self.__c = console(self.__spy, None)
        self.__c.input = self.__input

    def testPerformingSearchCallsSearchObject(self):
        self.__inputKey = "1"
        self.__c.SetSearchScreen(self.__spy)
        self.__c.Main()
        self.assertTrue(self.__spy.maincalled)

    def testListingByFirstLetterCallsFirstLetterObject(self):
        self.__inputKey = "2"
        self.__c.SetFirstLetterScreen(self.__spy)
        self.__c.Main()
        self.assertTrue(self.__spy.maincalled)

    def testDoingBookHarvestCallsAppObject(self):
        self.__inputKey = "3"
        self.__c.Main()
        self.assertTrue(self.__spy.harvestbookscalled)

    def __input(self):
        if not self.__alreadyInput:
            self.__alreadyInput = True
            return self.__inputKey
        else:
            return "0"


class Spy():
    def __init__(self):
        self.maincalled = False
        self.harvestbookscalled = False

    def Main(self):
        self.maincalled = True

    def HarvestBooks(self):
        self.harvestbookscalled = True



