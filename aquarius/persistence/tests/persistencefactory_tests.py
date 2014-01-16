#!/usr/bin/python3

import unittest
from aquarius.persistence.PersistenceFactory import PersistenceFactory
from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence


class persistenceFactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.f = PersistenceFactory(config_mock())
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        self.assertIsInstance(self.f.get_persistence("anyoldthing"), HardcodedPersistence)
        
    def testSqlLitePersistenceInstantiation(self):
        self.f.get_persistence("sqlite")


class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db"
        
