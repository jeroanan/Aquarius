from persistence.persistor import persistor

class persistencefactory(object):
        
    def GetPersistor(self):
        return persistor()
    
    
