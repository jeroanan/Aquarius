#!/usr/bin/python3

import unittest
from persistence.persistencefactory import persistencefactory
from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence

class PersistenceFactory_Tests(unittest.TestCase):
    
    def setUp(self):
        self.f = persistencefactory()        
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        self.assertIsInstance(self.f.GetPersistence("anyoldthing"), hardcodedpersistence)
        
if __name__=="__main__":
    unittest.main()