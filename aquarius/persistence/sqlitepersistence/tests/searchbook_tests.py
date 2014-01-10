import os
import unittest

from config import config
from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.addbook import addbook
from aquarius.persistence.sqlitepersistence.connection import connection
from aquarius.persistence.sqlitepersistence.searchbook import searchbook
from aquarius.persistence.sqlitepersistence.sqlitepersistence import persistence


class searchbook_tests(unittest.TestCase):
    
    def setUp(self):
        self.__conf = config()
        self.__conf.SqlLiteDatabasePath = "./database.db"
        self.__search = searchbook() 
        p = persistence(self.__conf, self.__search, addbook())        
        p.AddBook(self.__GetTreasureIsland())
    
    def __GetTreasureIsland(self):
        b = book()
        b.Id = 1
        b.Author = "Robert Louis Stevenson"
        b.Title = "Treasure Island"
        self.__AddFormats(b)
        return b
    
    def __AddFormats(self, b):
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "/dev/null"
        b.Formats.append(f)
        
    def tearDown(self):
        os.remove(self.__conf.SqlLiteDatabasePath)
            
    def testSearchBooksNoResultsReturnsNoResults(self):
        self.assertEqual(0, len(list(self.__doSearch("Moo"))))
    
    def testSearchForBooksNoResultsReturnsList(self):
        self.assertIsInstance(self.__doSearch("Moo"), list)
        
    def testSearchBooksBookFoundByTitleReturnsResults(self):
        self.assertEqual(1, len(list(self.__doSearch("Treasure"))))

    def testSearchBooksBookFoundByAuthorReturnsResults(self):
        self.assertEqual(1, len(list(self.__doSearch("Stevens"))))
        
    def testSearchBooksWithASubstringFromAuthorAndTitleOnlyReturnsOneResult(self):
        self.assertEqual(1, len(list(self.__doSearch("e"))))
        
    def testSearchBooksBookFoundGivesProperId(self):
        self.assertEqual(1, self.__doSearch("Treasure")[0].Id)      
          
    def testSearchBookGivesCorrectNumberOfFormats(self):
        self.assertEqual(1, len(self.__doSearch("Treasure")[0].Formats))   
    
    def __doSearch(self, searchTerm):
        with connection(self.__conf) as conn:
            return self.__search.SearchBooks(searchTerm, conn)
    
    def testGetBookDetailsReturnsEmptyBookForNonExistentBook(self):
        self.__assertGetBookDetailsGetsExpectedBook(1414, book())        
        
    def testGetBookDetailsReturnsBookForExistentBook(self):
        self.__assertGetBookDetailsGetsExpectedBook(1, self.__GetTreasureIsland())        
        
    def __assertGetBookDetailsGetsExpectedBook(self, bookId, expected):
        with connection(self.__conf) as conn:
            r = self.__search.GetBookDetails(bookId, conn)
        self.assertEqual(expected, r)
        
    def testGetBookDetailsReturnsCorrectBookFormatCode(self):
        with connection(self.__conf) as conn:
            r = self.__search.GetBookDetails(1, conn)
        self.assertEqual("EPUB", r.Formats[0].Format)
        
    def testGetBookDetailsReturnsCorrectLocation(self):
        with connection(self.__conf) as conn:
            r = self.__search.GetBookDetails(1, conn)
        self.assertEqual("/dev/null", r.Formats[0].Location)