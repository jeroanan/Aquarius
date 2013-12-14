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
    
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertEqual("<!DOCTYPE html>", str(teststring)[0:15])
    
    def testBookHandlerHtmlDocumentHasAppropriateTitle(self):
        html = self.h.BookHandler("1")
        title = self.__getFirstTagFoundByXPath(html, "./head/title")
        self.assertTrue(title.text.startswith(self.__testBookTitle))        
        
    def testBookHandlerHtmlDocumentContainsBookTitleHeading(self):
        html = self.h.BookHandler("1")
        h2 = self.__getFirstTagFoundByXPath(html, "./body/h2").text
        self.assertEqual(self.__testBookTitle, h2)
    
    def __getFirstTagFoundByXPath(self, xmlDoc, xPath):
        doc = etree.fromstring(xmlDoc)
        return doc.findall(xPath)[0]
        
    def testBookHandlerHtmlDocumentAuthorSectionsContainsTheAuthor(self):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        a = doc.findall("./body/div[@class='bookauthor']")[0]
        self.assertTrue(a.text.endswith(self.__testBookAuthor))
    
    def testBookHandlerHtmlDocumentContainsDownloadSection(self):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        a = doc.findall("./body/div[@class='downloads']")
        self.assertEquals(1, len(a))       
        
    def testBookHandlerHtmlDocumentDownloadSectionEpubDownloadAnchorTagContainsCorrectHref(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectDestination("epubdownload", "EPUB")
        
    def testBookHandlerHtmlDocumentDownloadSectionEpubDownloadAnchorTagContainsCorrectTitleAttribute(self):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        xp = "./body/div[@class='downloads']/p[@class='epubdownload']/a[@title='Download %s in EPUB Format']" 
        h =  xp % self.__testBookTitle
        d = doc.findall(h)
        self.assertEquals(1, len(d))
        
    def testBookHandlerHtmlDocumentDownloadSectionEpubDownloadAnchorTagContainsCorrectText(self):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        t = doc.findall("./body/div[@class='downloads']/p[@class='epubdownload']/a")[0].text
        self.assertEquals("EPUB", t)    
            
    def testBookHandlerHtmlDocumentDownloadSectionMobiDownloadAnchorTagContainsCorrectHref(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectDestination("mobidownload", "MOBI")
    
    def __assertFormatDownloadSectionAnchorTagHasCorrectDestination(self, sectionClass, formatCode):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        xp = "./body/div[@class='downloads']/p[@class='%s']/a[@href='/download?bookId=1&bookFormat=%s']"
        h = xp % (sectionClass, formatCode)
        d = doc.findall(h)
        self.assertEquals(1, len(d))
    
    def __GetXmlFromBookHandlerForBookWithAllFormats(self):
        return etree.fromstring(self.h.BookHandler("1"))
    
    class testApp(aquarius):
        
        def __init__(self):
            self.HarvestBooksCalled = False
            
        def HarvestBooks(self):
            self.HarvestBooksCalled = True