from aquarius.persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence
from aquarius.persistence.sqlitepersistence.sqlitepersistence import sqlitepersistence

class persistencefactory(object):
    
    def __init__(self, config):
        self.__config = config
    
    def GetPersistence(self, persistortype):
        if str.lower(persistortype) == "sqlite":
            return sqlitepersistence().GetInstance(self.__config)
        else:       
            return hardcodedpersistence(self.__config)    
