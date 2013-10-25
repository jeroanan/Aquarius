from aquarius import aquarius
from output.web.requesthandlers.requesthandler import requesthandler

import unittest

class RequestHandler_Tests(unittest.TestCase):
    
    def setUp(self):
        self.r = requesthandler(aquarius("hardcoded", None))

    def testCallIndexHandlerWebBrowserAgent(self):
        agentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
        returnXml = self.r.IndexHandler(agentString)
        self.assertEqual("<!DOCTYPE html>", str(returnXml)[0:15])    
    
    def testCallIndexHandlerOPDSAgent(self):
        agentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
        returnXml = self.r.IndexHandler(agentString)        
        self.assertEqual("<feed", returnXml.decode("utf-8")[0:5])
        
    def testCallByTitleHandlerOPDSAgent(self):
        agentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
        returnXml = self.r.ByTitleHandler(agentString)
        self.assertEqual("<feed", returnXml.decode("utf-8")[0:5])