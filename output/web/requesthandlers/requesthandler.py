from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler
from output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import xml.etree.ElementTree as etree

class requesthandler(object):
    
    def __init__(self, app):
        self.__app = app
        self.htmlHandler = htmlrequesthandler(app)
        self.opdsHandler = opdsrequesthandler(app)
        
    def IndexHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            return self.__stringFromEtree(self.opdsHandler.IndexHandler())
        return self.htmlHandler.IndexHandler()            
    
    def ByTitleHandler(self, userAgent):
        if self.__IsOpdsBrowser(userAgent):
            return self.__stringFromEtree(self.opdsHandler.ByTitleHandler())        
    
    def FirstLetterHandler(self, userAgent, letter):
        if self.__IsOpdsBrowser(userAgent):
            return self.__stringFromEtree(self.opdsHandler.FirstLetterHandler(letter))
    
    def BookHandler(self, userAgent, bookId):
        if self.__IsOpdsBrowser(userAgent):
            return self.__stringFromEtree(self.opdsHandler.BookHandler(bookId))
    
    def DownloadHandler(self, userAgent, bookId, bookFormat):
        if self.__IsOpdsBrowser(userAgent):
            return self.opdsHandler.DownloadHandler(bookId, bookFormat)
    
    def Search(self, userAgent, searchTerm):
        if self.__IsOpdsBrowser(userAgent):
            return self.__stringFromEtree(self.opdsHandler.Search(searchTerm))
        return self.htmlHandler.SearchHandler(searchTerm)

    def HarvestHandler(self):
        return self.htmlHandler.HarvestHandler()
            
    def __IsOpdsBrowser(self, userAgent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return userAgent.find("Aldiko")>-1

    def __stringFromEtree(self, inString):
        return etree.tostring(inString)
    