import unittest

from aquarius.output.console.firstletterscreen import firstletterscreen

class FirstLetterScreen_Tests(unittest.TestCase):
    
    def testCanInitialise(self):
        firstletterscreen(None)
