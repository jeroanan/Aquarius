import xml.etree.ElementTree as etree

from aquarius import aquarius
from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler

import unittest

class htmlrequesthandler_tests(unittest.TestCase):
    
    def setUp(self):
        self.h = htmlrequesthandler(aquarius("hardcoded", None, None))
        
    def testIndexHandler(self):
        self.__AssertIsHtmlDoc(self.h.IndexHandler())
        
    def testSearchHandler(self):
        self.__AssertIsHtmlDoc(self.h.SearchHandler("searchTerm"))
    
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertEqual("<!DOCTYPE html>", str(teststring)[0:15])
        
    def testSearchHandlerNoEntries(self):
        self.__assertNumberOfResultsFromSearchTerm("dfkjdslfjds", 0)       
    
    def testSearchHandlerEntriesFound(self):
        self.__assertNumberOfResultsFromSearchTerm("book", 1)
        
    def __assertNumberOfResultsFromSearchTerm(self, searchTerm, expectedNumberOfResults):
        r = self.h.SearchHandler(searchTerm)
        doc = etree.fromstring(r)
        body = doc.findall("body")
        self.assertEqual(expectedNumberOfResults + self.__getNumberOfHardcodedDivs(), len(body[0].findall("div")))
        
    def __getNumberOfHardcodedDivs(self):
        return 1