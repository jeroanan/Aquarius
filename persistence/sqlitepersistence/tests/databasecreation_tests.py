import os.path
import unittest
from persistence.sqlitepersistence.databasecreation import databasecreation
from persistence.sqlitepersistence.connection import connection

class databasecreation_tests(unittest.TestCase):   
    
    def test_createdb(self):
        d = databasecreation(config_mock())
        d.CreateDb()
        self.assertTrue(os.path.isfile(config_mock().SqlLiteDatabasePath))            
        
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 
    
