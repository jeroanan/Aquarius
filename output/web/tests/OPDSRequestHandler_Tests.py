from output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import unittest

class OPDSRequestHandler_Tests(unittest.TestCase):
    
    def testCanInitialise(self):
        r = opdsrequesthandler()
        
    @unittest.skip("waiting for basic opds functionality to be in place")
    def testIndexHandler(self):
        o = opdsrequesthandler()
        x = o.IndexHandler()
        self.assertEqual("<feed>", str(x)[0:6])