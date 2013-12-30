import os.path
import unittest
from config import config
from persistence.sqlitepersistence.databasecreation import databasecreation

class databasecreation_tests(unittest.TestCase):   
    
    def setUp(self):
        self.__conf = config()
        self.__conf.SqlLiteDatabasePath = "./database.db"
        
    def test_createdb(self):
        d = databasecreation(self.__conf)
        d.CreateDb()
        self.assertTrue(os.path.isfile(self.__conf.SqlLiteDatabasePath))
