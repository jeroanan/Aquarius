import os
import unittest
from persistence.sqlitepersistence.connection import connection
from persistence.sqlitepersistence.searchbook import searchbook
from persistence.sqlitepersistence.sqlitepersistence import persistence
from objects.book import book

class searchbook_tests(unittest.TestCase):
    
    def setUp(self):
        self.__persistence = searchbook(connection(config_mock()))
        self.__persistence = persistence(config_mock(), searchbook(connection(config_mock())))        
        self.__persistence.AddBook(self.__GetTreasureIsland())
    
    def __GetTreasureIsland(self):
        b = book()
        b.Id = 1
        b.Author = "Robert Louis Stevenson"
        b.Title = "Treasure Island"
        return b
    
    def tearDown(self):
        os.remove(config_mock().SqlLiteDatabasePath)
            
    def testSearchBooksNothingFound(self):
        r = self.__persistence.SearchBooks("Moo")
        self.assertEqual(0, self.__CountBooks(r))
    
    def testSearchBooksBookFoundByTitle(self):
        r = self.__persistence.SearchBooks("Treasure")
        self.assertEqual(1, self.__CountBooks(r))

    def testSearchBooksBookFoundByAuthor(self):
        r = self.__persistence.SearchBooks("Stevens")
        self.assertEqual(1, self.__CountBooks(r))
        
    def __CountBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
        
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 