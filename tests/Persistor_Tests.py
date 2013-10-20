#!/usr/bin/python3

import unittest
from persistence.persistor import persistor

class Persistor_Tests(unittest.TestCase):
    
    def setUp(self):
        self.p = persistor()
        
    def testSearchBooksNotImplemented(self):
        self.assertRaises(NotImplementedError, lambda: self.p.SearchBooks("Search term"))
        
    def testListBooksByFirstLetterNotImplemented(self):
        self.assertRaises(NotImplementedError, lambda: self.p.ListBooksByFirstLetter("A"))
        
    def testGetBookDetailsNotImplemented(self):
        self.assertRaises(NotImplementedError, lambda: self.p.GetBookDetails("1"))
        
if __name__=="__main__":
    unittest.main()