import unittest

from aquarius.output.console.ConsoleStrings import ConsoleStrings


class TestConsoleStrings(unittest.TestCase):
    """Unit tests of the ConsoleStrings class"""
    def setUp(self):
        """Common setup operations"""
        self.s = ConsoleStrings()
        
    def testGetMainMenu(self):
        """Given a request for the main menu, then get the main menu text"""
        text = self.s.get_main_menu()
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
        text = self.s.get_search_string()
        self.assertEqual("Search by book title: ", text)
        
    def testGetSearchResultTitleString(self):
        """Given some search results, then display the search results header"""
        text = self.s.get_search_result_title_string()
        self.assertEqual("""
        
Search Results
==============""", text)
        
    def testGetSearchResultFooterString(self):
        """Give some search results, when a certain number of items are in the
        results, then display the search results footer containing the number
        of results."""
        text = self.s.get_search_result_footer_string(45)
        self.assertEqual("""==============
45 result(s) found
        
        """, text)        
        
    def testGetFirstLetterString(self):
        """Given a First Letter command, then display the search books
        beginning with a letter string"""
        text = self.s.get_first_letter_string()
        self.assertEqual("Search for books beginning with: ", text)
