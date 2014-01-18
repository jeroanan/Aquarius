import unittest

from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence


class TestHardcodedPersistence(unittest.TestCase):
    """Unit tests for the HardcodedPersistence class"""
    def setUp(self):
        """Common setup operations"""
        self.p = HardcodedPersistence(None)
        
    def testSearchBooksNoResults(self):
        """Given a book search, when no matching book exists,
        then return an empty list"""
        result = self.p.search_books("Don't find me")
        self.assertEqual(0, self.__CountBooks(result))    

    def testSearchBooksWithResults(self):
        """Given a book search, when a matching book exists,
        then return the correct number of books"""
        result = self.p.search_books("oo")
        self.assertEqual(1, self.__CountBooks(result))
    
    def testSearchBooksEmptyString(self):
        """Given a book search, when an empty string
        is the search term, then return an empty list"""
        result = self.p.search_books("")
        self.assertEqual(0, self.__CountBooks(result))
        
    def testListBooksByFirstLetterNoneFound(self):
        """Given a search for books by first letter,
        when no matching books exist, then return an empty list"""
        result = self.p.list_books_by_first_letter("p")
        self.assertEqual(0, self.__CountBooks(result))        
    
    def testListBooksByFirstLetterResultsFound(self):
        """Given a search for books by first letter,
        when a matching book exists, then return the
        correct number of books"""
        result = self.p.list_books_by_first_letter("t")
        self.assertEqual(2, self.__CountBooks(result))
        
    def testGetBookDetailsBookDoesntExist(self):
        """Given a request for a book's details, when the book doesn't
        exist, then return None"""
        #TODO: propagation of null. change to empty set.
        result = self.p.get_book_details("-1")
        self.assertEqual(None, result)
        
    def testGetBookDetailsBookExists(self):
        """Given a request for a book's details, when the book exists,
        then return the correct book"""
        result = self.p.get_book_details("1")
        self.assertEqual(1, result.Id)       
    
    def testGetBookTypeDoesntExist(self):
        """Given a request for a book type, when the book type does not exist,
        then return None"""
        #TODO: propagation of null.
        t = self.p.get_book_type("exe")
        self.assertEqual(None, t)
        
    def testGetBookTypeExists(self):
        """Given a request for a book type, when the book type exists,
        then return it."""
        t = self.p.get_book_type("EPUB")
        self.assertEqual("EPUB", t.Format)
        
    def testAddBookDifferentFormatsJustOneInstanceOfBookExists(self):
        """Given the addition of the same book twice,
        when the formats are different,
        then just one record exists for the book,
        but two records exist for the format"""
        self.p.add_book(self.__GetFlyFishing("EPUB"))
        self.p.add_book(self.__GetFlyFishing("MOBI"))
        self.__CheckFlyFishingBookCount(1)
        self.__CheckFishingFormats(2)
        
    def testAddDuplicateBookDoesNotAddSecondFormat(self):
        """Given the addition of the same book twice,
        when the formats are the same,
        then just one record exists for the format"""
        self.p.add_book(self.__GetFlyFishing("EPUB"))
        self.p.add_book(self.__GetFlyFishing("EPUB"))
        self.__CheckFishingFormats(1)                      
    
    def __GetFlyFishing(self, formatcode):
        b = book()
        b.Title = "Fly Fishing"
        b.Author = "J. R. Hartley"
        b.AddFormat(self.__GetFormat(formatcode))
        return b
    
    def __CheckFishingFormats(self, expected):
        result = self.p.search_books("Fishing")
        self.assertEqual(expected, self.__CountFormats(result))
    
    def __CheckFlyFishingBookCount(self, expected):
        result = self.p.search_books("Fishing")
        self.assertEqual(expected, self.__CountBooks(result))
        
    @staticmethod
    def __GetFormat(formatcode):
        f = bookformat()
        f.Format = formatcode
        return f
           
    @staticmethod
    def __CountBooks(result):
        return len(list(result))        
    
    @staticmethod
    def __CountFormats(result):
        i = 0
        for b in result:
            i += len(list(b.Formats))
        return i
