from aquarius import aquarius
from output.web.requesthandlers.requesthandler import requesthandler

import unittest

class RequestHandler_Tests(unittest.TestCase):
    
    __webBrowserAgentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
    __opdsAgentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
    
    def setUp(self):
        self.r = requesthandler(aquarius("hardcoded", None))

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
        
