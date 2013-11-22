import os 
import unittest
from persistence.sqlitepersistence.sqlitepersistence import persistence

class sqlitepersistence_tests(unittest.TestCase):
    
    def setUp(self):
        self.__search = searchbook_mock()
        self.__persistence = persistence(config_mock(), self.__search)

    def tearDown(self):
        os.remove(config_mock().SqlLiteDatabasePath)
        
    def testSearchBooks(self):
        self.__persistence.SearchBooks("Moo")
        self.assertEqual(1, self.__search.searchCount)    
    
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 
        
class searchbook_mock(object):
    
    def __init__(self):
        self.searchCount = 0
    
    def SearchBooks(self, searchTerm):
        self.searchCount += 1