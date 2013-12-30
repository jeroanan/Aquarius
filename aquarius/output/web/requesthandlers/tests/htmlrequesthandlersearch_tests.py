import unittest
import xml.etree.ElementTree as etree

from aquarius import aquarius

from output.web.requesthandlers.htmlrequesthandlersearch import htmlrequesthandlersearch

class htmlrequesthandlersearch_tests(unittest.TestCase):

    def setUp(self):
        self.h = htmlrequesthandlersearch(aquarius("hardcoded", None, None))        
        self.__testBookTitle = "The Book with no name"
        self.__testBookAuthor = "An Author"
        
    def testSearchHandler(self):
        self.__AssertIsHtmlDoc(self.h.Handle("searchTerm"))
    
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
    
    def testSearchResultTitleHyperLinkDestination(self):
        self.__assertBookHyperlinkAttributeValue("booktitle", "href", "/book?bookId=1")
        
    def testSearchResultTitleHyperlinkTitle(self):
        self.__assertBookHyperlinkAttributeValue("booktitle", "title", "%s - %s" % \
                                                  (self.__testBookAuthor, self.__testBookTitle))
        
    def testSearchResultTitleHyperlinkText(self):
        body = self.__doSearchGetBody("book")
        self.assertEqual(self.__testBookTitle, \
                         body.findall("./div[@class='searchresult']/p[@class='booktitle']/a")[0].text)
    
    def testSearchResultAuthorStartsWithAuthor(self):
        body = self.__doSearchGetBody("book")
        self.assertTrue(\
                body.findall("./div[@class='searchresult']/p[@class='bookauthor']")[0].text.startswith("Author: "))
    
    def testSearchResultsAuthorHyperlinkDestination(self):
        self.__assertBookHyperlinkAttributeValue("bookauthor", "href", \
                                                 "/search?searchTerm=%s" % self.__testBookAuthor)       
    
    def testSearchResultsAuthorHyperlinkTitle(self):
        self.__assertBookHyperlinkAttributeValue("bookauthor", "title", "Search for %s" % self.__testBookAuthor)
        
    def testSearchResultsAuthorHyperlinkText(self):
        body = self.__doSearchGetBody("book")
        self.assertEqual(self.__testBookAuthor, \
                         body.findall("./div[@class='searchresult']/p[@class='bookauthor']/a")[0].text)
    
    def testSearchResultsDownloadHyperlinkHasHyperlink(self):
        body = self.__doSearchGetBody("book")
        self.assertEquals(1, len(body.findall("./div[@class='searchresult']/p[@class='bookdownload']/a")))
    
    def testSearchResultsDownloadHyperlinkDestination(self):
        self.__assertBookHyperlinkAttributeValue("bookdownload", "href", "")
    
    def testSearchResultsDownloadHyperlinkTitle(self):
        self.__assertBookHyperlinkAttributeValue("bookdownload", "title",\
                    "Quick download links for %s" % self.__testBookTitle)
    
    def testSearchResultsDownloadHyperlinkText(self):
        body = self.__doSearchGetBody("book")
        body = self.assertEqual("Download", \
                                body.findall("./div[@class='searchresult']/p[@class='bookdownload']/a")[0].text)
        
    def __assertBookHyperlinkAttributeValue(self, parentClass, attr, val):
        body = self.__doSearchGetBody("book")
        self.assertEqual(1, len(body.findall(self.__getBookHyperlinkXPath() % (parentClass, attr, val))))
    
    def __getBookHyperlinkXPath(self):
        return "./div[@class='searchresult']/p[@class='%s']/a[@%s='%s']"    
    
    def testNumberOfResultsParagraphExists(self):
        body = self.__doSearchGetBody("book")
        self.assertEqual(1, len(body.findall("./p[@class='resultcount']")))
        
    def testNumberOfResultsStartsWithResultsFound(self):
        body = self.__doSearchGetBody("book")
        self.assertTrue(body.findall("./p[@class='resultcount']")[0].text.startswith("Books found: "))
    
    def testNumberOfResultsIsCorrectWithResults(self):
        body = self.__doSearchGetBody("book")
        self.assertTrue(body.findall("./p[@class='resultcount']")[0].text.endswith(" 1"))
    
    def __doSearchGetBody(self, searchTerm):
        r = self.h.Handle(searchTerm)
        doc = etree.fromstring(r)
        return doc.findall("body")[0]