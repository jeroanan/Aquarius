class requesthandler:
    
    
    def IndexHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            pass
        else:
            pass
    
    def __IsOpdsBrowser(self, userAgent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return userAgent.find("Aldiko")>-1
    
    
