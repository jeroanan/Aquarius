#!/usr/bin/python3

import unittest
from output.console.consolestrings import consolestrings

class ConsoleStrings_Tests(unittest.TestCase):
    
    def setUp(self):
        self.s = consolestrings()
        
    def testGetMainMenu(self):
        text = self.s.GetMainMenu()
        self.assertEqual("""Main Menu
        =========
        1. Search for books
        2. List books starting with...
        =========
        Please enter option:""", text)
        
if __name__=="__main__":
    unittest.main()