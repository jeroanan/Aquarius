#!/usr/bin/python3

import unittest
from persistence.persistencefactory import persistencefactory
from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence

class PersistenceFactory_Tests(unittest.TestCase):
    
    def setUp(self):
        self.f = persistencefactory(config_mock())        
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        self.assertIsInstance(self.f.GetPersistence("anyoldthing"), hardcodedpersistence)
        
    def testSqlLitePersistenceInstantiation(self):
        self.f.GetPersistence("sqlite")
    
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db"
        
if __name__=="__main__":
    unittest.main()