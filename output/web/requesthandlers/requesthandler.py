from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler
from output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import xml.etree.ElementTree as etree

class requesthandler(object):
    
    def __init__(self, app):
        self.__app = app
    
    def IndexHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler(self.__app).IndexHandler())
        return htmlrequesthandler().IndexHandler()            
    
    def ByTitleHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler(self.__app).ByTitleHandler())        
    
    def FirstLetterHandler(self, userAgent, letter):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler(self.__app).FirstLetterHandler(letter))
    
    def BookHandler(self, userAgent, bookId):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler(self.__app).BookHandler(bookId))
    
    def DownloadHandler(self, userAgent, bookId, bookFormat):
        if self.__IsOpdsBrowser(userAgent):
            return opdsrequesthandler(self.__app).DownloadHandler(bookId, bookFormat)
    
    def Search(self, userAgent, searchTerm):
        if self.__IsOpdsBrowser(userAgent):
            return etree.tostring(opdsrequesthandler(self.__app).Search(searchTerm))
        return htmlrequesthandler().SearchHandler(searchTerm)
    
    def __IsOpdsBrowser(self, userAgent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return userAgent.find("Aldiko")>-1
