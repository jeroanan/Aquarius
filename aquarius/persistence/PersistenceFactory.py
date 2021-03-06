from aquarius.persistence.sqlitepersistence.QueryFactory import QueryFactory
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class PersistenceFactory(object):

    def __init__(self, config):
        self.__config = config

    def get_persistence(self):
        return SqlitePersistence(QueryFactory())

