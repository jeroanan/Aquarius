from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence
from persistence.sqlitepersistence.sqlitepersistence import sqlitepersistence

class persistencefactory(object):
    
    def __init__(self, config):
        self.__config = config
    
    def GetPersistence(self, persistortype):
        if str.lower(persistortype) == "sqlite":
            return sqlitepersistence(self.__config)        
        return hardcodedpersistence(self.__config)    
