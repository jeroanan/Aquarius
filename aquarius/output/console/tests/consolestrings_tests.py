import unittest

from aquarius.output.console.consolestrings import consolestrings

class ConsoleStrings_Tests(unittest.TestCase):
    
    def setUp(self):
        self.s = consolestrings()
        
    def testGetMainMenu(self):
        text = self.s.GetMainMenu()
        self.assertEqual("""Main Menu
=========
1. Search for books
2. List books starting with...
3. Perform Harvest
0. Exit
=========
Please enter option:""", text)
        
    def testGetSearchString(self):
        text = self.s.GetSearchString()
        self.assertEqual("Search by book title: ", text)
        
    def testGetSearchResultTitleString(self):
        text = self.s.GetSearchResultTitleString()
        self.assertEqual("""
        
Search Results
==============""", text)
        
    def testGetSearchResultFooterString(self):
        text = self.s.GetSearchResultFooterString(45)
        self.assertEqual("""==============
45 result(s) found
        
        """, text)        
        
    def testGetFirstLetterString(self):
        text = self.s.GetFirstLetterString()
        self.assertEqual("Search for books beginning with: ", text)
    