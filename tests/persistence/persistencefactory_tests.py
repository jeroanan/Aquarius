import unittest

from aquarius.persistence.PersistenceFactory import PersistenceFactory
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestPersistenceFactory(unittest.TestCase):
    def setUp(self):
        self.__target = PersistenceFactory(ConfigMock())
        
    def test_factory_gives_sqlite_persistor(self):
        self.assertIsInstance(self.__target.get_persistence(), SqlitePersistence)


class ConfigMock(object):

    def __init__(self):
        self.sqllite_database_path = "./database.db"
