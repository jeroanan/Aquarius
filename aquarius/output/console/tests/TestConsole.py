import unittest

from aquarius.output.console.console import console


class TestConsole(unittest.TestCase):
    """Unit tests for the Console class"""
    def setUp(self):
        """Common setup operations"""
        self.__inputKey = 0
        self.__alreadyInput = False
        self.__spy = Spy()
        self.__c = console(self.__spy, None)
        self.__c.input = self.__input

    def testPerformingSearchCallsSearchObject(self):
        """Given a search command, then the main method of the
        search object is called."""
        self.__inputKey = "1"
        self.__c.SetSearchScreen(self.__spy)
        self.__c.Main()
        self.assertTrue(self.__spy.maincalled)

    def testListingByFirstLetterCallsFirstLetterObject(self):
        """Given a first letter command, the main method of the
        first letter object is called"""
        self.__inputKey = "2"
        self.__c.SetFirstLetterScreen(self.__spy)
        self.__c.Main()
        self.assertTrue(self.__spy.maincalled)

    def testDoingBookHarvestCallsAppObject(self):
        """Given a harvest books command, the main method of the
        harvest books object is called."""
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



