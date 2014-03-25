import unittest

from aquarius.persistence.PersistenceFactory import PersistenceFactory
from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence


class TestPersistenceFactory(unittest.TestCase):
    def setUp(self):
        self.f = PersistenceFactory(ConfigMock())
        
    def test_factory_gives_hardcoded_persistor_by_default(self):
        self.assertIsInstance(self.f.get_persistence("anyoldthing"), HardcodedPersistence)
        
    def test_sqlite_persistence_instantiation(self):
        self.f.get_persistence("sqlite")


class ConfigMock(object):

    def __init__(self):
        self.sqllite_database_path = "./database.db"
