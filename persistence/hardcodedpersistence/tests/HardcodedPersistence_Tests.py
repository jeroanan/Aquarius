#!/usr/bin/python3

import unittest
from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence

class HardcodedPersistence_Tests(unittest.TestCase):
    
    def setUp(self):
        self.p = hardcodedpersistence()        
        
    def testSearchBooksNoResults(self):
        result = self.p.SearchBooks("Don't find me")        
        self.assertEqual(0, self.__CountResults(result))    

    def testSearchBooksWithResults(self):
        result = self.p.SearchBooks("oo")                
        self.assertEqual(1, self.__CountResults(result))
    
    def testSearchBooksEmptyString(self):
        result = self.p.SearchBooks("")
        self.assertEqual(0, self.__CountResults(result))
        
    def testListBooksByFirstLetterNoneFound(self):
        result = self.p.ListBooksByFirstLetter("p")
        self.assertEqual(0, self.__CountResults(result))        
    
    def testListBooksByFirstLetterResultsFound(self):
        result = self.p.ListBooksByFirstLetter("t")
        self.assertEqual(1, self.__CountResults(result))
        
    def testGetBookDetailsBookDoesntExist(self):
        result = self.p.GetBookDetails("-1")
        self.assertEqual(None, result)
        
    def testGetBookDetailsBookExists(self):
        result = self.p.GetBookDetails("1")
        self.assertEqual(1, result.Id)       
    
    def testGetBookTypeDosntExist(self):
        t = self.p.GetBookType("exe")
        self.assertEqual(None, t)
        
    def testGetBookTypeExists(self):
        t = self.p.GetBookType("EPUB")
        self.assertEqual("EPUB", t.Format)
        
    def __CountResults(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
        
if __name__=="__main__":
    unittest.main()