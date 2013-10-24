from output.web.requesthandlers.requesthandler import requesthandler
import unittest

class RequestHandler_Tests(unittest.TestCase):
    
    def setUp(self):
        self.r = requesthandler()

    def testCallIndexHandlerWebBrowserAgent(self):
        agentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
        returnXml = self.r.IndexHandler(agentString)
        self.assertEqual("<!DOCTYPE html>", str(returnXml)[0:15])
    
    @unittest.skip("Waiting for supporting object to be finished")
    def testCallIndexHandlerOPDSAgent(self):
        agentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
        returnXml = self.r.IndexHandler(agentString)
        self.assertEqual("<feed>", str(returnXml)[0:6])