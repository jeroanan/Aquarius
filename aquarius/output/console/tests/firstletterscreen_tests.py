import unittest

from aquarius.output.console.firstletterscreen import firstletterscreen
from aquarius.output.console.tests.AquariusDummy import AquariusDummy
from aquarius.output.console.tests.ConsoleStringsMock import ConsoleStringsMock


class firstletterscreen_tests(unittest.TestCase):
    
    def testCanInitialise(self):
        firstletterscreen(AquariusDummy())

    def testMainListsByFirstLetter(self):
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

