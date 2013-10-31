from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence
from persistence.sqlitepersistence.sqlitepersistence import sqlitepersistence

class persistencefactory(object):
        
    def GetPersistence(self, persistortype):
        if str.lower(persistortype) == "sqlite":
            return sqlitepersistence()
        
        return hardcodedpersistence()    
