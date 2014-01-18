import os
import unittest

from Config import Config
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.SqlitePersistence import Persistence


class TestSearchBook(unittest.TestCase):
   #TODO: pydoc
    def setUp(self):
        self.__conf = Config()
        self.__conf.sqllite_database_path = "./database.db"
        self.__search = SearchBook()
        p = Persistence(self.__conf, self.__search, AddBook())
        p.add_book(self.__GetTreasureIsland())
    
    def __GetTreasureIsland(self):
        b = Book()
        b.id = 1
        b.author = "Robert Louis Stevenson"
        b.title = "Treasure Island"
        self.__AddFormats(b)
        return b
    
    def __AddFormats(self, b):
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "/dev/null"
        b.formats.append(f)
        
    def tearDown(self):
        os.remove(self.__conf.sqllite_database_path)
            
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
        self.assertEqual(1, self.__doSearch("Treasure")[0].id)
          
    def testSearchBookGivesCorrectNumberOfFormats(self):
        self.assertEqual(1, len(self.__doSearch("Treasure")[0].formats))
    
    def __doSearch(self, searchTerm):
        with Connection(self.__conf) as conn:
            return self.__search.search_books(searchTerm, conn)
    
    def testGetBookDetailsReturnsEmptyBookForNonExistentBook(self):
        self.__assertGetBookDetailsGetsExpectedBook(1414, Book())
        
    def testGetBookDetailsReturnsBookForExistentBook(self):
        self.__assertGetBookDetailsGetsExpectedBook(1, self.__GetTreasureIsland())        
        
    def __assertGetBookDetailsGetsExpectedBook(self, bookId, expected):
        with Connection(self.__conf) as conn:
            r = self.__search.get_book_details(bookId, conn)
        self.assertEqual(expected, r)
        
    def testGetBookDetailsReturnsCorrectBookFormatCode(self):
        with Connection(self.__conf) as conn:
            r = self.__search.get_book_details(1, conn)
        self.assertEqual("EPUB", r.formats[0].Format)
        
    def testGetBookDetailsReturnsCorrectLocation(self):
        with Connection(self.__conf) as conn:
            r = self.__search.get_book_details(1, conn)
        self.assertEqual("/dev/null", r.formats[0].Location)