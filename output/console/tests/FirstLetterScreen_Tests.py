#!/usr/bin/python3
from output.console.firstletterscreen import firstletterscreen
import unittest

class FirstLetterScreen_Tests(unittest.TestCase):
    
    def testCanInitialise(self):
        firstletterscreen(None)

if __name__=="__main__":
    unittest.main()