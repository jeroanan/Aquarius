#!/usr/bin/python3

import unittest
from aquarius.persistence.persistencefactory import persistencefactory
from aquarius.persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence

class persistenceFactory_tests(unittest.TestCase):
    
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