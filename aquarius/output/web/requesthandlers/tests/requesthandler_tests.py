from aquarius.aquarius import aquarius
from aquarius.output.web.requesthandlers.requesthandler import requesthandler

import unittest

class requesthandler_tests(unittest.TestCase):
    
    __webBrowserAgentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
    __opdsAgentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
    
    def setUp(self):
        self.r = requesthandler(aquarius("hardcoded", None, None))

    def testCallingIndexHandlerWithAWebBrowserAgentReturnsAHtmlDocument(self):
        self.__assertIsAnHtmlPage(self.r.IndexHandler(self.__webBrowserAgentString))
        
    def testCallingIndexHandlerWithAnOpdsAgentReturnsAnOpdsFeed(self):
        self.__assertIsAnOpdsFeed(self.r.IndexHandler(self.__opdsAgentString))
        
    def testCallingByTitleHandlerWithAnOpdsAgentReturnsAnOpdsFeed(self):
        self.__assertIsAnOpdsFeed(self.r.ByTitleHandler(self.__opdsAgentString))
        
    def testCallingFirstLetterHandlerWithAnOpdsAgentReturnsAnOpdsFeed(self):
        self.__assertIsAnOpdsFeed(self.r.FirstLetterHandler(self.__opdsAgentString, "t"))
        
    def testCallingFirstLetterHandlerWithAHtmlAgentReturnsAHtmlDocument(self):
        self.__assertIsAnHtmlPage(self.r.FirstLetterHandler(self.__webBrowserAgentString, "t"))
        
    def testCallingBookHandlerWithAnOpdsAgentReturnsAnOpdsFeed(self):
        self.__assertIsAnOpdsFeed(self.r.BookHandler(self.__opdsAgentString, "1"))
        
    def testCallingBookHandlerWithAHtmlAgentReturnsAHtmlDocument(self):
        self.__assertIsAnHtmlPage(self.r.BookHandler(self.__webBrowserAgentString, "1"))
    
    def testCallingDownloadHandlerWithAnOPDSAgentReturnsAnOpdsFeed(self):
        self.assertNotEqual(None, self.r.DownloadHandler(self.__opdsAgentString, "1", "EPUB"))
        
    def testCallingSearchHandlerWithAnOpdsAgentReturnsAnOpdsFeed(self):
        self.__assertIsAnOpdsFeed(self.r.Search(self.__opdsAgentString, "oo"))
        
    def testCallingSearchHandlerWithAWebBrowserAgentReturnsAHtmlDocument(self):
        self.__assertIsAnHtmlPage(self.r.Search(self.__webBrowserAgentString, "oo"))
        
    def testCallingHarvestHandlerWithAWebBrowserAgentReturnsAHtmlDocument(self):
        self.__assertIsAnHtmlPage(self.r.HarvestHandler())
    
    def __assertIsAnOpdsFeed(self, testString):
        self.assertTrue(str.startswith(testString.decode("utf-8"), "<feed"))
        
    def __assertIsAnHtmlPage(self, testString):
        self.assertTrue(str.startswith(testString, "<!DOCTYPE html>"))
        