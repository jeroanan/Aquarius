#!/usr/bin/python3

import unittest
from persistence.persistencefactory import persistencefactory
from persistence.persistor import persistor
from persistence.hardcodedpersistor import hardcodedpersistor

class PersistenceFactory_Tests(unittest.TestCase):
    
    def setUp(self):
        self.f = persistencefactory()        
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        self.assertIsInstance(self.f.GetPersistor("anyoldthing"), hardcodedpersistor)
        
if __name__=="__main__":
    unittest.main()