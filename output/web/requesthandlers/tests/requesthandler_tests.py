from aquarius import aquarius
from output.web.requesthandlers.requesthandler import requesthandler

import unittest

class requesthandler_tests(unittest.TestCase):
    
    __webBrowserAgentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
    __opdsAgentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
    
    def setUp(self):
        self.r = requesthandler(aquarius("hardcoded", None, None))

    def testCallIndexHandlerWebBrowserAgent(self):
        returnXml = self.r.IndexHandler(self.__webBrowserAgentString)
        self.assertEqual("<!DOCTYPE html>", str(returnXml)[0:15])    
    
    def testCallIndexHandlerOPDSAgent(self):
        returnXml = self.r.IndexHandler(self.__opdsAgentString)        
        self.assertEqual("<feed", returnXml.decode("utf-8")[0:5])
        
    def testCallByTitleHandlerOPDSAgent(self):
        returnXml = self.r.ByTitleHandler(self.__opdsAgentString)
        self.assertEqual("<feed", returnXml.decode("utf-8")[0:5])
        
    def testCallFirstLetterHandlerOPDSAgent(self):
        returnXml = self.r.FirstLetterHandler(self.__opdsAgentString, "t")
        self.assertEqual("<feed", returnXml.decode("utf-8")[0:5])
        
    def testCallBookHandlerOPDSAgent(self):
        returnXml = self.r.BookHandler(self.__opdsAgentString, "1")
        self.assertEqual("<feed", returnXml.decode("utf-8")[0:5])
        
    def testCallDownloadHandlerOPDSAgent(self):
        returnXml = self.r.DownloadHandler(self.__opdsAgentString, "1", "EPUB")
        self.assertNotEqual(None, returnXml)
        
    def testCallSearchHandlerOPDSAgent(self):
        returnXml = self.r.Search(self.__opdsAgentString, "oo")
        self.assertEqual("<feed", returnXml.decode("utf-8")[0:5])
        
    @unittest.skip
    def testCallSearchHandlerWebBrowserAgent(self):
        returnXml = self.r.Search(self.__webBrowserAgentString, "oo")
        self.assertEqual("<!DOCTYPE html>", str(returnXml)[0:15])
        