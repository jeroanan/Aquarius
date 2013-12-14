from aquarius import aquarius
from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler
import xml.etree.ElementTree as etree

import unittest

class htmlrequesthandler_tests(unittest.TestCase):
    
    def setUp(self):
        self.h = htmlrequesthandler(aquarius("hardcoded", None, None))
        self.__testBookTitle = "The Book with no name"
        self.__testBookAuthor = "An Author"
        
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
    
    def testBookHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.h.BookHandler("1"))
    
    def testBookHandlerHtmlDocumentHasAppropriateTitle(self):
        html = self.h.BookHandler("1")
        doc = etree.fromstring(html)
        title = doc.findall("./head/title")[0]
        self.assertTrue(title.text.startswith(self.__testBookTitle))        
        
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertEqual("<!DOCTYPE html>", str(teststring)[0:15])
        
    class testApp(aquarius):
        
        def __init__(self):
            self.HarvestBooksCalled = False
            
        def HarvestBooks(self):
            self.HarvestBooksCalled = True