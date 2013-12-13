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

    def tearDown(self):
        os.remove(config_mock().SqlLiteDatabasePath)
        
    def testAddingTwoIdenticalBooksCausesOnlyOneToBeWrittenn(self):
        b = book()
        b.Title = "Treasure Island"
        b.Author = "Robert Louis Stevenson"
        self.__persistence.AddBook(b)
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
    
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 
        
class searchbook_mock(object):
    
    def __init__(self):
        self.searchCount = 0
    
    def SearchBooks(self, searchTerm):
        self.searchCount += 1