from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler

import unittest

class htmlrequesthandler_tests(unittest.TestCase):
    
    def testInitialise(self):
        h = htmlrequesthandler()
        
    def testIndexHandler(self):
        h = htmlrequesthandler()
        x = h.IndexHandler()
        self.assertEqual("<!DOCTYPE html>", str(x)[0:15])
        
    def testSearchHandler(self):
        h = htmlrequesthandler()
        x = h.SearchHandler()
        self.assertEqual("<!DOCTYPE html>", str(x)[0:15])