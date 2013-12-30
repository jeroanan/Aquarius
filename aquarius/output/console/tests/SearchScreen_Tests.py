import unittest

from aquarius.output.console.searchscreen import searchscreen

class SearchScreen_Tests(unittest.TestCase):
    
    def testCanInitialise(self):
        searchscreen(None)
