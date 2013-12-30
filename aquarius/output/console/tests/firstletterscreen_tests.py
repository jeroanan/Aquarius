import unittest

from aquarius.output.console.firstletterscreen import firstletterscreen

class firstletterscreen_tests(unittest.TestCase):
    
    def testCanInitialise(self):
        firstletterscreen(None)
