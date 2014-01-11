import unittest

from aquarius.output.console.consolestrings import consolestrings


class TestConsoleStrings(unittest.TestCase):
    """Unit tests of the ConsoleStrings class"""
    def setUp(self):
        """Common setup operations"""
        self.s = consolestrings()
        
    def testGetMainMenu(self):
        """Given a request for the main menu, then get the main menu text"""
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
        """Given a request for a search by book title, then get the search by
        book title text"""
        text = self.s.GetSearchString()
        self.assertEqual("Search by book title: ", text)
        
    def testGetSearchResultTitleString(self):
        """Given some search results, then display the search results header"""
        text = self.s.GetSearchResultTitleString()
        self.assertEqual("""
        
Search Results
==============""", text)
        
    def testGetSearchResultFooterString(self):
        """Give some search results, when a certain number of items are in the
        results, then display the search results footer containing the number
        of results."""
        text = self.s.GetSearchResultFooterString(45)
        self.assertEqual("""==============
45 result(s) found
        
        """, text)        
        
    def testGetFirstLetterString(self):
        """Given a First Letter command, then display the search books
        beginning with a letter string"""
        text = self.s.GetFirstLetterString()
        self.assertEqual("Search for books beginning with: ", text)
