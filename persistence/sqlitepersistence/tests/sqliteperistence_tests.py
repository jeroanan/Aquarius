import os 
import unittest

from objects.book import book
from persistence.sqlitepersistence.connection import connection
from persistence.sqlitepersistence.searchbook import searchbook
from persistence.sqlitepersistence.sqlitepersistence import persistence

class sqlitepersistence_tests(unittest.TestCase):
    
    def setUp(self):
        conf = config_mock()
        conn = connection(conf)
        self.__persistence = persistence(conf, searchbook(conn))
        self.__persistence.AddBook(self.__GetTreasureIsland())
        
    def tearDown(self):
        os.remove(config_mock().SqlLiteDatabasePath)
        
    def testAddingTwoIdenticalBooksCausesOnlyOneToBeWritten(self):
        b = self.__GetTreasureIsland()
        self.__persistence.AddBook(b)
        r = self.__persistence.SearchBooks("Treasure")
        self.assertEqual(1, self.__countResult(r))
        
    def __countResult(self, resultSet):
        i = 0
        for result in resultSet:
            i+=1
        return i
    
    def testSearchingBooksCausesTheSearchMethodToBeCalled(self):
        s = searchbook_mock()
        p = persistence(config_mock(), s)
        p.SearchBooks("Moo")
        self.assertEqual(1, s.searchCount)    
    
    def testCanCallGetBookDetails(self):
        self.__persistence.GetBookDetails("1")
    
    def testGetBookDetailsReturnsTheCorrectBook(self):
        book = self.__persistence.GetBookDetails("1")
        self.assertEqual(self.__GetTreasureIsland(), book)
    
    def testGetBookDetailsReturnsEmptyBookIfTheBookDoesntExist(self):
        b = book()
        result = self.__persistence.GetBookDetails("1337")
        self.assertEqual(b, result)    
    
    def testAddingBookCausesItsFormatsToBeAdded(self):
        b = self.__GetTreasureIsland()
        b.Formats.append("EPUB")
        self.__persistence.AddBook(b)
        r = self.__persistence.SearchBooks("Treasure")[0]
        self.assertEqual(1, len(r.Formats))
    
    def testAddingABookThenTheSameBookWithADifferentFormatCausesBothFormatsToBeAdded(self):        
        b = self.__GetTreasureIsland()
        b.Formats.append("EPUB")
        self.__persistence.AddBook(b)
        c = self.__GetTreasureIsland()
        c.Formats.append("MOBI")
        self.__persistence.AddBook(c)
        r = self.__persistence.SearchBooks("Treasure")[0]
        self.assertEqual(2, len(r.Formats))
        
    def __GetTreasureIsland(self):
        b = book()
        b.Id = "1"
        b.Title = "Treasure Island"
        b.Author = "Robert Louis Stevenson"
        return b
    
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 
        
class searchbook_mock(object):
    
    def __init__(self):
        self.searchCount = 0
    
    def SearchBooks(self, searchTerm):
        self.searchCount += 1