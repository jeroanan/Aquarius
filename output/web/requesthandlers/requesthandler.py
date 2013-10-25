from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler
from output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import xml.etree.ElementTree as etree

class requesthandler(object):
    
    def __init__(self, app):
        self.__app = app
    
    def IndexHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler(self.__app).IndexHandler())
        else:
            return htmlrequesthandler().IndexHandler()            
    
    def ByTitleHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler(self.__app).ByTitleHandler())        
    
    def __IsOpdsBrowser(self, userAgent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return userAgent.find("Aldiko")>-1
    