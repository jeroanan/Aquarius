import os.path
import unittest
from Config import Config
from aquarius.persistence.sqlitepersistence.DatabaseCreation import DatabaseCreation


class TestDatabaseCreation(unittest.TestCase):

    def setUp(self):
        self.__conf = Config()
        self.__conf.sqllite_database_path = "./database.db"
        
    def test_createdb(self):
        d = DatabaseCreation(self.__conf)
        d.create_db()
        self.assertTrue(os.path.isfile(self.__conf.sqllite_database_path))
