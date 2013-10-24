from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler

class requesthandler(object):
    
    def IndexHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            pass
        else:
            return htmlrequesthandler().IndexHandler()            
    
    def __IsOpdsBrowser(self, userAgent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return userAgent.find("Aldiko")>-1
    
    
