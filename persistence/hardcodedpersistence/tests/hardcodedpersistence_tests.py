#!/usr/bin/python3

import unittest
from objects.book import book
from objects.bookformat import bookformat
from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence
from decimal import InvalidOperation

class HardcodedPersistence_Tests(unittest.TestCase):
    
    def setUp(self):
        self.p = hardcodedpersistence(None)        
        
    def testSearchBooksNoResults(self):
        result = self.p.SearchBooks("Don't find me")        
        self.assertEqual(0, self.__CountBooks(result))    

    def testSearchBooksWithResults(self):
        result = self.p.SearchBooks("oo")                
        self.assertEqual(1, self.__CountBooks(result))
    
    def testSearchBooksEmptyString(self):
        result = self.p.SearchBooks("")
        self.assertEqual(0, self.__CountBooks(result))
        
    def testListBooksByFirstLetterNoneFound(self):
        result = self.p.ListBooksByFirstLetter("p")
        self.assertEqual(0, self.__CountBooks(result))        
    
    def testListBooksByFirstLetterResultsFound(self):
        result = self.p.ListBooksByFirstLetter("t")
        self.assertEqual(1, self.__CountBooks(result))
        
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
        
    def testAddBookDifferentFormatsJustOneInstanceOfBookExists(self):        
        b1 = self.__GetFlyFishing("EPUB")
        b2 = self.__GetFlyFishing("MOBI")        
        self.p.AddBook(b1)
        self.p.AddBook(b2)
        result = self.p.SearchBooks("Fishing")
        self.assertEqual(1, self.__CountBooks(result))
        result = self.p.SearchBooks("Fishing")     
        self.assertEqual(2, self.__CountFormats(result))
        
    def testAddDuplicateBookDoesNotAddSecondFormat(self):
        b1 = self.__GetFlyFishing("EPUB")
        b2 = self.__GetFlyFishing("EPUB")
        self.p.AddBook(b1)
        self.p.AddBook(b2)
        result = self.p.SearchBooks("Fishing")
        self.assertEqual(1, self.__CountFormats(result))                         
        
    def __GetFlyFishing(self, formatcode):
        b = book()
        b.Title = "Fly Fishing"
        b.Author = "J. R. Hartley"
        b.Formats = [self.__GetFormat(formatcode)]
        return b
    
    def __GetFormat(self, formatcode):
        f = bookformat()
        f.Format = formatcode
        return f
           
    def __CountBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
    
    def __CountFormats(self, result):        
        i = 0
        for book in result:
            for bf in book.Formats:
                i += 1
            return i
        return 0
        
if __name__=="__main__":
    unittest.main()