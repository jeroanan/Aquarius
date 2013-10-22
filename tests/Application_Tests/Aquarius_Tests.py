#!/usr/bin/python3

import unittest
from aquarius import aquarius

class aquarius_tests(unittest.TestCase):
    
    def setUp(self):
        self.__app = aquarius("persistor", "console")
        self.__gotCallback = False
        
    def testSearchBooks(self):
        self.__app.SearchBooks("", self.__callback)
        self.assertTrue(self.__gotCallback, "Did not get callback")
        
    def testListBooksByFirstLetter(self):
        self.__app.ListBooksByFirstLetter("b", self.__callback)
        self.assertTrue(self.__gotCallback, "Did not get callback")
        
    def testGetBookDetails(self):        
        self.__app.GetBookDetails(0, self.__callback)
        self.assertTrue(self.__gotCallback, "Did not get callback")
                    
    def testGetBook(self):
        self.__app.GetBook(1, self.__callback)
        
    def __countBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
    
    def __callback(self, inval):
        self.__gotCallback = True
    
if __name__=="__main__":
    unittest.main()