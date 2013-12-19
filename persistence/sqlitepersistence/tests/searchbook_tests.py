import os
import unittest

from config import config
from persistence.sqlitepersistence.addbook import addbook
from persistence.sqlitepersistence.searchbook import searchbook
from persistence.sqlitepersistence.sqlitepersistence import persistence
from objects.book import book

class searchbook_tests(unittest.TestCase):
    
    def setUp(self):
        self.__conf = config()
        self.__conf.SqlLiteDatabasePath = "./database.db" 
        self.__persistence = persistence(self.__conf, searchbook(), addbook())        
        self.__persistence.AddBook(self.__GetTreasureIsland())
    
    def __GetTreasureIsland(self):
        b = book()
        b.Id = 1
        b.Author = "Robert Louis Stevenson"
        b.Title = "Treasure Island"
        return b
    
    def tearDown(self):
        os.remove(self.__conf.SqlLiteDatabasePath)
            
    def testSearchBooksNoResultsReturnsNoResults(self):
        r = self.__persistence.SearchBooks("Moo")
        self.assertEqual(0, self.__CountBooks(r))
    
    def testSearchForBooksNoResultsReturnsList(self):
        r = self.__persistence.SearchBooks("Moo")
        self.assertIsInstance(r, list)
        
    def testSearchBooksBookFoundByTitleReturnsResults(self):
        r = self.__persistence.SearchBooks("Treasure")
        self.assertEqual(1, self.__CountBooks(r))

    def testSearchBooksBookFoundByAuthorReturnsResults(self):
        r = self.__persistence.SearchBooks("Stevens")
        self.assertEqual(1, self.__CountBooks(r))
        
    def testSearchBooksWithASubstringFromAuthorAndTitleOnlyReturnsOneResult(self):
        r = self.__persistence.SearchBooks("e")
        self.assertEqual(1, self.__CountBooks(r))
        
    def testSearchBooksBookFoundGivesProperId(self):
        r = self.__persistence.SearchBooks("Treasure")
        self.assertEqual(1, r[0].Id)
        
    def __CountBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
        
    def testSearchBooksBookFoundReturnsListOfBooks(self):
        r = self.__persistence.SearchBooks("Treasure")
        self.assertIsInstance(r, list)      
