from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class PersistenceFactory(object):

    def __init__(self, config):
        self.__config = config
    
    def get_persistence(self, persistor_type):
        if persistor_type == "sqlite":
            return SqlitePersistence()
        else:       
            return HardcodedPersistence()
