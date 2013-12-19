import os
import unittest

from objects.book import book
from persistence.sqlitepersistence.addbook import addbook
from persistence.sqlitepersistence.connection import connection
from persistence.sqlitepersistence.searchbook import searchbook
from persistence.sqlitepersistence.sqlitepersistence import persistence

class addbook_tests(unittest.TestCase):
    
    def setUp(self):
        self.__a = addbook()
        self.__conf = config_mock()
        self.__conn = connection(self.__conf)
        self.__p = persistence(self.__conf, searchbook(), addbook())
        
    def tearDown(self):
        os.remove(config_mock().SqlLiteDatabasePath)
        
    def testAddingTwoIdenticalBooksCausesOnlyOneToBeWritten(self):
        b = self.__GetTreasureIsland()
        with connection(self.__conf) as conn:
            self.__a.AddBook(b, conn)
        r = self.__p.SearchBooks("Treasure")
        self.assertEqual(1, len(list(r)))
        
    def testAddingBookCausesItsFormatsToBeAdded(self):
        with connection(self.__conf) as conn:
            self.__a.AddBook(self.__GetTreasureIslandWithFormat("EPUB"), conn)
        r = self.__p.SearchBooks("Treasure")[0]
        self.assertEqual(1, len(r.Formats))
    
    def testAddingABookThenTheSameBookWithADifferentFormatCausesBothFormatsToBeAdded(self):
        with connection(self.__conf) as conn:        
            self.__a.AddBook(self.__GetTreasureIslandWithFormat("EPUB"), conn)
            self.__a.AddBook(self.__GetTreasureIslandWithFormat("MOBI"), conn)
        r = self.__p.SearchBooks("Treasure")[0]
        self.assertEqual(2, len(r.Formats))
        
    def __GetTreasureIslandWithFormat(self, formatCode):
        b = self.__GetTreasureIsland()
        b.Formats.append(formatCode)
        return b
    
    def __GetTreasureIsland(self):
        b = book()
        b.Id = "1"
        b.Title = "Treasure Island"
        b.Author = "Robert Louis Stevenson"
        return b
    
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 