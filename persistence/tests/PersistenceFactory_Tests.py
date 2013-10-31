#!/usr/bin/python3

import unittest
from persistence.persistencefactory import persistencefactory
from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence
from persistence.sqlitepersistence.sqlitepersistence import sqlitepersistence
from config import config

class PersistenceFactory_Tests(unittest.TestCase):
    
    def setUp(self):
        self.f = persistencefactory(config())        
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        self.assertIsInstance(self.f.GetPersistence("anyoldthing"), hardcodedpersistence)
        
    def testFactoryGivesSqlitePersistorWhenAsked(self):
        self.assertIsInstance(self.f.GetPersistence("sqlite"), sqlitepersistence)
        
if __name__=="__main__":
    unittest.main()