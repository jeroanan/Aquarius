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
    
    def __assertNumberOfResultsFromSearchTerm(self, searchTerm, expectedNumberOfResults):
        body = self.__doSearchGetBody(searchTerm)
        self.assertEqual(self.__getTotalExpectedDivs(expectedNumberOfResults), len(body.findall("div")))
        
    def __getTotalExpectedDivs(self, expectedNumberOfResults):
        return expectedNumberOfResults + self.__getNumberOfHardcodedDivs()
        
    def __getNumberOfHardcodedDivs(self):
        return 1
    
    def testSearchResultHasTitleParagraph(self):
        self.__assertSearchResultHasParagraphWithClass("booktitle")       
            
    def testSearchResultHasAuthorParagraph(self):
        self.__assertSearchResultHasParagraphWithClass("bookauthor")
    
    def testSearchResultHasQuickDownloadParagraph(self):
        self.__assertSearchResultHasParagraphWithClass("bookdownload")
    
    def __assertSearchResultHasParagraphWithClass(self, className):
        body = self.__doSearchGetBody("book")
        self.assertEqual(1, len(body.findall("./div[@class='searchresult']/p[@class='%s']" % className)))
    
    def __doSearchGetBody(self, searchTerm):
        r = self.h.SearchHandler(searchTerm)
        doc = etree.fromstring(r)
        return doc.findall("body")[0]
    
    
    
        