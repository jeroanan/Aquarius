#!/usr/bin/python3

import unittest
from aquarius import aquarius

class aquarius_tests(unittest.TestCase):
    
    def setUp(self):
        self.__app = aquarius("persistor", "console")
        self.__gotCallback = False
        
    def testSearchBooks(self):
        self.__app.SearchBooks("")
        
    def testListBooksByFirstLetter(self):
        self.__app.ListBooksByFirstLetter("b")
        
    def testGetBookDetails(self):        
        self.__app.GetBookDetails(0)
                        
    def testGetBookType(self):
        self.__app.GetBookType("EPUB")
        
    def testHarvestBooks(self):
        self.__app.HarvestBooks()

    def testAddBook(self):
        self.__app.AddBook(None)
        
    def __countBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
        
if __name__=="__main__":
    unittest.main()