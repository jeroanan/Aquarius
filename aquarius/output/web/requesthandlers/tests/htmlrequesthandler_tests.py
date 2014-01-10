import unittest
from unittest.mock import Mock

from aquarius.aquarius import aquarius
from aquarius.output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler


class htmlrequesthandler_tests(unittest.TestCase):
    
    def setUp(self):
        self.__a = aquarius("hardcoded", None, None)
        self.__a.HarvestBooks = Mock(return_value=None)        
        self.__h = htmlrequesthandler(self.__a)
        
    def testIndexHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__h.IndexHandler())
        
    def testSearchHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__h.SearchHandler("searchTerm"))
    
    def testHarvestHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__h.HarvestHandler())
    
    def testHarvestHandlerCallsHarvestBooks(self):
        self.__h.HarvestHandler()
        self.assertTrue(self.__a.HarvestBooks.called)        
    
    def testBookHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__h.BookHandler("1"))
    
    def testDownloadHandlerReturnsSomething(self):
        b = self.__h.DownloadHandler("1", "EPUB")        
        self.assertGreater(len(b), 0)

    def testFirstLetterHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__h.FirstLetterHandler("T"))
        
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertTrue(teststring.startswith("<!DOCTYPE html>"))
