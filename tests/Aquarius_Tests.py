#!/usr/bin/python3

import unittest
from aquarius import aquarius

class aquarius_tests(unittest.TestCase):
    
    def setUp(self):
        self.app = aquarius()
        
    def testSearchBooksEmpyString(self):
        result = self.app.SearchBooks("")            
        self.assertEqual(0, self.__countBooks(result))    

    def testSearchBooksWithMatchesFound(self):
        result = self.app.SearchBooks("book")            
        self.assertEqual(1, self.__countBooks(result))
        
    def testSearchBooksWithNoMatchesFound(self):
        result = self.app.SearchBooks("not app book")            
        self.assertEqual(0, self.__countBooks(result))
    
    def testListBooksByFirstLetterNoMatchesFound(self):
        result = self.app.ListBooksByFirstLetter("n")
        self.assertEqual(0,self.__countBooks(result))
        
    def testListBooksByFirstLetterMatchesFound(self):
        result = self.app.ListBooksByFirstLetter("b")
        self.assertEqual(1, self.__countBooks(result))       
    
    def testGetBookDetailsBookDoesntExist(self):        
        self.assertEqual(None, self.app.GetBookDetails(0))
        
    def testGetBookDetailsBookFound(self):
        self.assertNotEqual(None, self.app.GetBookDetails(1))
    
    def __countBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
    
if __name__=="__main__":
    unittest.main()