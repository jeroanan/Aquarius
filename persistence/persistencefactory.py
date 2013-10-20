from persistence.hardcodedpersistence.hardcodedpersistence import hardcodedpersistence

class persistencefactory(object):
        
    def GetPersistence(self, persistortype):
        return hardcodedpersistence()    
