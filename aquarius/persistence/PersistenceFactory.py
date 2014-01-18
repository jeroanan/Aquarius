from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class PersistenceFactory(object):
    """Return the correct persistor based on the string given"""
    def __init__(self, config):
        """Set initial object state"""
        self.__config = config
    
    def get_persistence(self, persistor_type):
        """Return the correct persistor based on the string given"""
        if str.lower(persistor_type) == "sqlite":
            return SqlitePersistence().get_instance(self.__config)
        else:       
            return HardcodedPersistence(self.__config)
