import unittest
from persistence.sqlitepersistence.connection import connection

class connection_tests(unittest.TestCase):

    def testExecuteSqlFetchAllNoResults(self):
        with connection(config_mock()) as conn:
            result = conn.ExecuteSqlFetchAll("SELECT 1 WHERE 1=0")
        self.assertEqual(0, len(list(result)))
        
    def testExecuteSqlFetchAllResultsFound(self):
        with connection(config_mock()) as conn:
            result = conn.ExecuteSqlFetchAll("SELECT 1")
        self.assertEqual(1, len(list(result)))    
    
    def testExecuteSql(self):
        with connection(config_mock()) as conn:
            conn.ExecuteSql("SELECT 1")
        
    def testCanExecuteGetLastRowId(self):
        with connection(config_mock()) as conn:
            conn.GetLastRowId()
        
    def testGetLastRowIdReturnsNoneWhenNoInsertMade(self):
        with connection(config_mock()) as conn:
            self.assertIsNone(conn.GetLastRowId())    

    def testGetLastRowReturnsCorrectRowId(self):        
        with connection(config_mock()) as conn:
            self.__setupTestData(conn)
            self.assertEqual(1, conn.GetLastRowId())
            
    def __setupTestData(self, conn):        
        conn.ExecuteSql("CREATE TABLE IF NOT EXISTS Test (ID INTEGER PRIMARY KEY ASC, Desc TEXT);")
        conn.ExecuteSql("INSERT INTO Test (Desc) VALUES ('foo');")
        
class config_mock(object):
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 