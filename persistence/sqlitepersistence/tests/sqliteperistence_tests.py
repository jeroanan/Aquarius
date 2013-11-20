from persistence.sqlitepersistence.sqlitepersistence import sqlitepersistence
from objects.book import book
import unittest

class sqlitepersistence_tests(unittest.TestCase):
    
    def setUp(self):
        self.o = sqlitepersistence(config_mock())        
        self.o.AddBook(self.__GetTreasureIsland())
    
    def testSearchBooksNothingFound(self):
        r = self.o.SearchBooks("Moo")
        self.assertEqual(0, self.__CountBooks(r))
    
    def testSearchBooksBookFoundByTitle(self):
        r = self.o.SearchBooks("Treasure")
        self.assertEqual(1, self.__CountBooks(r))
        
    def __GetTreasureIsland(self):
        b = book()
        b.Id = 1
        b.Author = "Robert Louis Stevenson"
        b.Title = "Treasure Island"
        return b
    
    def __CountBooks(self, result):
        i = 0
        for book in result:
            i += 1        
        return i
    
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 