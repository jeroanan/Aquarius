import os

from Config import Config
import unittest
from aquarius.persistence.sqlitepersistence.Connection import Connection


class TestConnection(unittest.TestCase):

    def setUp(self):
        self.__conf = Config()
        self.__conf.sqllite_database_path = "./database.db"
    
    def tearDown(self):
        os.remove(self.__conf.sqllite_database_path)
        
    def testExecuteSqlFetchAllNoResults(self):
        with Connection(self.__conf) as conn:
            result = conn.execute_sql_fetch_all("SELECT 1 WHERE 1=0")
        self.assertEqual(0, len(list(result)))
        
    def testExecuteSqlFetchAllResultsFound(self):
        with Connection(self.__conf) as conn:
            result = conn.execute_sql_fetch_all("SELECT 1")
        self.assertEqual(1, len(list(result)))    
    
    def testExecuteSql(self):
        with Connection(self.__conf) as conn:
            conn.execute_sql("SELECT 1")
        
    def testCanExecuteGetLastRowId(self):
        with Connection(self.__conf) as conn:
            conn.get_last_row_id()
        
    def testGetLastRowIdReturnsNoneWhenNoInsertMade(self):
        with Connection(self.__conf) as conn:
            self.assertIsNone(conn.get_last_row_id())

    def testGetLastRowReturnsCorrectRowId(self):        
        with Connection(self.__conf) as conn:
            self.__setupTestData(conn)
            self.assertEqual(1, conn.get_last_row_id())
            
    @staticmethod
    def __setupTestData(conn):
        conn.execute_sql("CREATE TABLE IF NOT EXISTS Test (ID INTEGER PRIMARY KEY ASC, Desc TEXT);")
        conn.execute_sql("INSERT INTO Test (Desc) VALUES ('foo');")