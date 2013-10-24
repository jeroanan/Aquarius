from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler
from output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import xml.etree.ElementTree as etree

class requesthandler(object):
    
    def IndexHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler().IndexHandler())
        else:
            return htmlrequesthandler().IndexHandler()            
    
    def __IsOpdsBrowser(self, userAgent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return userAgent.find("Aldiko")>-1
    
    
    