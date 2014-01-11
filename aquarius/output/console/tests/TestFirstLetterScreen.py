import unittest

from aquarius.output.console.firstletterscreen import firstletterscreen
from aquarius.output.console.tests.AquariusDummy import AquariusDummy
from aquarius.output.console.tests.ConsoleStringsMock import ConsoleStringsMock


class TestFirstLetterScreen(unittest.TestCase):
    """Unit tests for the First Letter Screen"""
    def testMainListsByFirstLetter(self):
        """Given a call to the first letter screen, then the fir letter
        screen is rendered"""
        self.__arrange()
        self.__f.Main()
        self.AssertFirstLetterScreenRendered()

    def __arrange(self):
        self.__a = AquariusDummy()
        self.__f = firstletterscreen(self.__a)
        self.__strings = ConsoleStringsMock()
        self.__f.SetStringsObject(self.__strings)
        self.__f.input = lambda: None

    def AssertFirstLetterScreenRendered(self):
        self.assertTrue(self.__strings.verify_printedfirstletterscreen())
        self.assertTrue(self.__a.listbooksbyfirstlettercalled)

