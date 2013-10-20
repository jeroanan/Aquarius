from persistence.hardcodedpersistence import hardcodedpersistence

class persistencefactory(object):
        
    def GetPersistor(self, persistortype):
        return hardcodedpersistence()
    
    
