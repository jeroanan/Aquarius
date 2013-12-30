import unittest

from aquarius.output.console.searchscreen import searchscreen

class searchscreen_tests(unittest.TestCase):
    
    def testCanInitialise(self):
        searchscreen(None)
