import unittest

from aquarius.output.console.firstletterscreen import firstletterscreen
from aquarius.output.console.tests.AquariusDummy import AquariusDummy
from aquarius.output.console.tests.ConsoleStringsMock import ConsoleStringsMock


class firstletterscreen_tests(unittest.TestCase):
    
    def testCanInitialise(self):
        firstletterscreen(AquariusDummy())

    def testMainListsByFirstLetter(self):
        a = AquariusDummy()
        f = firstletterscreen(a)
        strings = ConsoleStringsMock()
        f.SetStringsObject(strings)
        f.input = lambda: None
        f.Main()
        self.assertTrue(strings.verify_printedfirstletterscreen())
        self.assertTrue(a.listbooksbyfirstlettercalled)

