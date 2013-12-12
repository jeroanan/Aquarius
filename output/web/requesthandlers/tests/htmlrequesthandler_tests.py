

from aquarius import aquarius
from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler

import unittest

class htmlrequesthandler_tests(unittest.TestCase):
    
    def setUp(self):
        self.h = htmlrequesthandler(aquarius("hardcoded", None, None))
        
    def testIndexHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.h.IndexHandler())
        
    def testSearchHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.h.SearchHandler("searchTerm"))
    
    def testHarvestHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.h.HarvestHandler())
    
    def testHarvestHandlerCallsHarvestBooks(self):
        a = self.testApp()
        htmlrequesthandler(a).HarvestHandler()
        self.assertTrue(a.HarvestBooksCalled)
    
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertEqual("<!DOCTYPE html>", str(teststring)[0:15])
        
    class testApp(aquarius):
        
        def __init__(self):
            self.HarvestBooksCalled = False
            
        def HarvestBooks(self):
            self.HarvestBooksCalled = True