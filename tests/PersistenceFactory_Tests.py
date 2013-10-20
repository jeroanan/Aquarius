#!/usr/bin/python3

import unittest
from persistence.persistencefactory import persistencefactory
from persistence.hardcodedpersistence import hardcodedpersistence

class PersistenceFactory_Tests(unittest.TestCase):
    
    def setUp(self):
        self.f = persistencefactory()        
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        self.assertIsInstance(self.f.GetPersistor("anyoldthing"), hardcodedpersistence)
        
if __name__=="__main__":
    unittest.main()