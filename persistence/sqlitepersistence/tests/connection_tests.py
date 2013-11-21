import os
import unittest
from persistence.sqlitepersistence.connection import connection

class connection_tests(unittest.TestCase):
    
    def setUp(self):
        self.conn = connection(config_mock())
        
    def tearDown(self):
        os.remove(config_mock().SqlLiteDatabasePath)

    def testExecuteSqlFetchAllNoResults(self):
        result = self.conn.ExecuteSqlFetchAll("SELECT 1 WHERE 1=0")
        self.assertEqual(0, self.__countResults(result))
        
    def testExecuteSqlFetchAllResultsFound(self):
        result = self.conn.ExecuteSqlFetchAll("SELECT 1")
        self.assertEqual(1, self.__countResults(result))

    def __countResults(self, result):
        resultCounter = 0
        for entry in result:
            resultCounter += 1        
        return resultCounter
            
    def testExecuteSql(self):
        self.conn.ExecuteSql("SELECT 1")
    
class config_mock(object):
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 