#!/usr/bin/python3
from output.console.searchscreen import searchscreen
import unittest

class SearchScreen_Tests(unittest.TestCase):
    
    def testCanInitialise(self):
        searchscreen(None)

if __name__=="__main__":
    unittest.main()