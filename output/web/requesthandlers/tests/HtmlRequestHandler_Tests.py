from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler

import unittest

class HtmlRequestHandler_Tests(unittest.TestCase):
    
    def testInitialise(self):
        h = htmlrequesthandler()
        
    def testIndexHandler(self):
        h = htmlrequesthandler()
        x = h.IndexHandler()
        self.assertEqual("<!DOCTYPE html>", str(x)[0:15])