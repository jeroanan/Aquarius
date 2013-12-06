from aquarius import aquarius
from output.web.requesthandlers.requesthandler import requesthandler

import unittest

class requesthandler_tests(unittest.TestCase):
    
    __webBrowserAgentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
    __opdsAgentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
    
    def setUp(self):
        self.r = requesthandler(aquarius("hardcoded", None, None))

    def testCallIndexHandlerWebBrowserAgent(self):
        self.assertIsAnHtmlPage(self.r.IndexHandler(self.__webBrowserAgentString))
        
    def testCallIndexHandlerOPDSAgent(self):
        self.assertIsAnOpdsFeed(self.r.IndexHandler(self.__opdsAgentString))
        
    def testCallByTitleHandlerOPDSAgent(self):
        self.assertIsAnOpdsFeed(self.r.ByTitleHandler(self.__opdsAgentString))
        
    def testCallFirstLetterHandlerOPDSAgent(self):
        self.assertIsAnOpdsFeed(self.r.FirstLetterHandler(self.__opdsAgentString, "t"))
        
    def testCallBookHandlerOPDSAgent(self):
        self.assertIsAnOpdsFeed(self.r.BookHandler(self.__opdsAgentString, "1"))
        
    def testCallDownloadHandlerOPDSAgent(self):
        self.assertNotEqual(None, self.r.DownloadHandler(self.__opdsAgentString, "1", "EPUB"))
        
    def testCallSearchHandlerOPDSAgent(self):
        self.assertIsAnOpdsFeed(self.r.Search(self.__opdsAgentString, "oo"))
        
    def testCallSearchHandlerWebBrowserAgent(self):
        self.assertIsAnHtmlPage(self.r.Search(self.__webBrowserAgentString, "oo"))
        
    def assertIsAnOpdsFeed(self, testString):
        self.assertEqual("<feed", testString.decode("utf-8")[0:5])
        
    def assertIsAnHtmlPage(self, testString):
        self.assertEqual("<!DOCTYPE html>", str(testString)[0:15])
        