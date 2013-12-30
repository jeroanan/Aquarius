import os

from config import config
import unittest
from aquarius.persistence.sqlitepersistence.connection import connection

class connection_tests(unittest.TestCase):

    def setUp(self):
        self.__conf = config()
        self.__conf.SqlLiteDatabasePath = "./database.db"
    
    def tearDown(self):
        os.remove(self.__conf.SqlLiteDatabasePath)
        
    def testExecuteSqlFetchAllNoResults(self):
        with connection(self.__conf) as conn:
            result = conn.ExecuteSqlFetchAll("SELECT 1 WHERE 1=0")
        self.assertEqual(0, len(list(result)))
        
    def testExecuteSqlFetchAllResultsFound(self):
        with connection(self.__conf) as conn:
            result = conn.ExecuteSqlFetchAll("SELECT 1")
        self.assertEqual(1, len(list(result)))    
    
    def testExecuteSql(self):
        with connection(self.__conf) as conn:
            conn.ExecuteSql("SELECT 1")
        
    def testCanExecuteGetLastRowId(self):
        with connection(self.__conf) as conn:
            conn.GetLastRowId()
        
    def testGetLastRowIdReturnsNoneWhenNoInsertMade(self):
        with connection(self.__conf) as conn:
            self.assertIsNone(conn.GetLastRowId())    

    def testGetLastRowReturnsCorrectRowId(self):        
        with connection(self.__conf) as conn:
            self.__setupTestData(conn)
            self.assertEqual(1, conn.GetLastRowId())
            
    def __setupTestData(self, conn):        
        conn.ExecuteSql("CREATE TABLE IF NOT EXISTS Test (ID INTEGER PRIMARY KEY ASC, Desc TEXT);")
        conn.ExecuteSql("INSERT INTO Test (Desc) VALUES ('foo');") 