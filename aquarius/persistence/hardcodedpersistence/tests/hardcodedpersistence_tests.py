import unittest

from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence

class hardcodedpersistence_tests(unittest.TestCase):
    
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
        self.assertEqual(2, self.__CountBooks(result))
        
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
        self.p.AddBook(self.__GetFlyFishing("EPUB"))
        self.p.AddBook(self.__GetFlyFishing("MOBI"))
        self.__CheckFlyFishingBookCount(1)
        self.__CheckFishingFormats(2)
        
    def testAddDuplicateBookDoesNotAddSecondFormat(self):
        self.p.AddBook(self.__GetFlyFishing("EPUB"))
        self.p.AddBook(self.__GetFlyFishing("EPUB"))
        self.__CheckFishingFormats(1)                      
    
    def __GetFlyFishing(self, formatcode):
        b = book()
        b.Title = "Fly Fishing"
        b.Author = "J. R. Hartley"
        b.AddFormat(self.__GetFormat(formatcode))
        return b
    
    def __CheckFishingFormats(self, expected):
        result = self.p.SearchBooks("Fishing")
        self.assertEqual(expected, self.__CountFormats(result))
    
    def __CheckFlyFishingBookCount(self, expected):
        result = self.p.SearchBooks("Fishing")
        self.assertEqual(expected, self.__CountBooks(result))
        
    def __GetFormat(self, formatcode):
        f = bookformat()
        f.Format = formatcode
        return f
           
    def __CountBooks(self, result):
        return len(list(result))        
    
    def __CountFormats(self, result):
        i = 0
        for book in result:
            i += len(list(book.Formats))
        return i
        