#!/usr/bin/python3

import unittest
from aquarius import aquarius

class aquarius_tests(unittest.TestCase):
    
    def setUp(self):
        self.app = aquarius("persistor")
        
    def testSearchBooks(self):
        self.app.SearchBooks("")
        
    def testListBooks(self):
        self.app.ListBooksByFirstLetter("b")
        
    def testGetBookDetails(self):        
        self.app.GetBookDetails(0)
                    
    def testGetBook(self):
        self.app.GetBook(1)
        
    def __countBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
    
if __name__=="__main__":
    unittest.main()