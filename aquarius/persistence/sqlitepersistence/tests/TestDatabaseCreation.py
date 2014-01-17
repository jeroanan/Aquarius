import os.path
import unittest
from Config import Config
from aquarius.persistence.sqlitepersistence.databasecreation import databasecreation


class TestDatabaseCreation(unittest.TestCase):
    
    def setUp(self):
        self.__conf = Config()
        self.__conf.sqllite_database_path = "./database.db"
        
    def test_createdb(self):
        d = databasecreation(self.__conf)
        d.CreateDb()
        self.assertTrue(os.path.isfile(self.__conf.sqllite_database_path))
