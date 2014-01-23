#!/usr/bin/python3

import unittest

from aquarius.persistence.PersistenceFactory import PersistenceFactory
from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence


class TestPersistenceFactory(unittest.TestCase):
    def setUp(self):
        self.f = PersistenceFactory(ConfigMock())
        
    def testFactoryGivesHardcodedPersistorByDefault(self):
        """Given a request for a persistor, when it's unrecognised, then return
        the hardcoded persistor"""
        self.assertIsInstance(self.f.get_persistence("anyoldthing"), HardcodedPersistence)
        
    def testSqlLitePersistenceInstantiation(self):
        """Given a request for a persistor, when it's for the sqlite persistor,
        then return the sqlite persistor"""
        self.f.get_persistence("sqlite")


class ConfigMock(object):
    """Test double for the Config class"""
    def __init__(self):
        """Set initial object state"""
        self.sqllite_database_path = "./database.db"

