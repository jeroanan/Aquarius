#!/usr/bin/python3

import unittest
from aquarius.persistence.persistencefactory import persistencefactory
from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence


class persistenceFactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.f = persistencefactory(config_mock())        
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        self.assertIsInstance(self.f.GetPersistence("anyoldthing"), HardcodedPersistence)
        
    def testSqlLitePersistenceInstantiation(self):
        self.f.GetPersistence("sqlite")


class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db"
        
