from persistence.hardcodedpersistor import hardcodedpersistor

class persistencefactory(object):
        
    def GetPersistor(self, persistortype):
        return hardcodedpersistor()
    
    
