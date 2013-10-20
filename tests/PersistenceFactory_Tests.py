#!/usr/bin/python3

import unittest
from persistence.persistencefactory import persistencefactory
from persistence.persistor import persistor

class PersistenceFactory_Tests(unittest.TestCase):
    
    def setUp(self):
        self.f = persistencefactory()
        
    def testFactoryGivesValidPersistor(self):
        self.assertIsInstance(self.f.GetPersistor(), persistor)
        
if __name__=="__main__":
    unittest.main()