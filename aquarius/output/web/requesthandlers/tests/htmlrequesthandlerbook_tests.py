import unittest
import xml.etree.ElementTree as etree

from aquarius import aquarius
from output.web.requesthandlers.htmlrequesthandlerbook import htmlrequesthandlerbook

class htmlrequesthandlerbook_tests(unittest.TestCase):
    
    def setUp(self):
        self.__testBookTitle = "The Book with no name"
        self.__testBookAuthor = "An Author"
        self.__handler = htmlrequesthandlerbook(aquarius("hardcoded", None, None))
        
    def testBookHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__handler.Handle("1"))
    
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertEqual("<!DOCTYPE html>", str(teststring)[0:15])
    
    def testBookHandlerHtmlDocumentHasAppropriateTitle(self):
        html = self.__handler.Handle("1")
        title = self.__getFirstTagFoundByXPath(html, "./head/title")
        self.assertTrue(title.text.startswith(self.__testBookTitle))
        
    def testBookHandlerHtmlDocumentContainsBookTitleHeading(self):
        html = self.__handler.Handle("1")
        h2 = self.__getFirstTagFoundByXPath(html, "./body/h2").text
        self.assertEqual(self.__testBookTitle, h2)    
    
    def __getFirstTagFoundByXPath(self, xmlDoc, xPath):
        doc = etree.fromstring(xmlDoc)
        return doc.findall(xPath)[0]
        
    def testBookHandlerHtmlDocumentAuthorSectionsContainsTheAuthor(self):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        a = doc.findall("./body/div[@class='bookauthor']")[0]
        self.assertTrue(a.text.endswith(self.__testBookAuthor))

    def testBookHandlerHtmlDocumentDownloadSectionEpubDownloadAnchorTagContainsCorrectHref(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectDestination("epubdownload", "EPUB")
    
    def testBookHandlerHtmlDocumentDownloadSectionEpubDownloadAnchorTagContainsCorrectTitle(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectTitle("epubdownload", "EPUB")    
        
    def testBookHandlerHtmlDocumentDownloadSectionEpubDownloadAnchorTagContainsCorrectText(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectText("epubdownload", "EPUB")
        
    def testBookHandlerHtmlDocumentDownloadSectionContainsNoEpubSectionWhenBookIsNotEpub(self):
        doc = self.__GetXmlFromBookHandlerForBookWithNoFormats()
        e = doc.findall("./body/div[@class='downloads']/p[@class='epubdownload']")
        self.assertEqual(0, len(e))
    
    def testBookHandlerHtmlDocumentDownloadSectionMobiDownloadAnchorTagContainsCorrectHref(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectDestination("mobidownload", "MOBI")
        
    def testBookHandlerHtmlDocumentDownloadSectionMobiDownloadAnchorTagContainsCorrectTitle(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectTitle("mobidownload", "MOBI")       
    
    def testBookHandlerHtmlDocumentDownloadSectionMobiDownloadAnchorTagContainsCorrectText(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectText("mobidownload", "MOBI")
                
    def testBookHandlerHtmlDocumentDownloadSectionContainsNoMobiSectionWhenBookIsNotMobi(self):
        self.__assertDownloadLinkNotInapprorpiatelyDisplayed("mobidownload")
        
    def testBookHandlerHtmlDocumentDownloadSectionPdfDownloadAnchorTagContainsCorrectHref(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectDestination("pdfdownload", "PDF")
        
    def testBookHandlerHtmlDocumentDownloadSectionPdfDownloadAnchorTagContainsCorrectTitle(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectTitle("pdfdownload", "PDF")
        
    def testBookHandlerHtmlDocumentDownloadSectionPdfDownloadAnchorTagContainsCorrectText(self):
        self.__assertFormatDownloadSectionAnchorTagHasCorrectText("pdfdownload", "PDF")
    
    def testBookHandlerHtmlDocumentDownloadSectionContainsNoPdfSectionWhenBookIsNotPdf(self):
        self.__assertDownloadLinkNotInapprorpiatelyDisplayed("pdfdownload")
        
    def __assertFormatDownloadSectionAnchorTagHasCorrectTitle(self, sectionClass, formatCode):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        xp = "./body/div[@class='downloads']/p[@class='%s']/a[@title='Download %s in %s Format']" 
        h =  xp % (sectionClass, self.__testBookTitle, formatCode)
        self.__assertExecutingXPathGetsOneElement(doc, h)
    
    def __assertFormatDownloadSectionAnchorTagHasCorrectDestination(self, sectionClass, formatCode):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        xp = "./body/div[@class='downloads']/p[@class='%s']/a[@href='/download?bookId=1&bookFormat=%s']"
        h = xp % (sectionClass, formatCode)
        self.__assertExecutingXPathGetsOneElement(doc, h)    

    def __assertExecutingXPathGetsOneElement(self, doc, xpath):
        x = doc.findall(xpath)
        self.assertEquals(1, len(x))
                
    def __assertFormatDownloadSectionAnchorTagHasCorrectText(self, sectionClass, formatCode):
        doc = self.__GetXmlFromBookHandlerForBookWithAllFormats()
        t = doc.findall("./body/div[@class='downloads']/p[@class='%s']/a" % sectionClass)[0].text
        self.assertEquals(formatCode, t)
    
    def __assertDownloadLinkNotInapprorpiatelyDisplayed(self, sectionClass):
        doc = self.__GetXmlFromBookHandlerForBookWithNoFormats()
        e = doc.findall("./body/div[@class='downloads']/p[@class='%s']" % sectionClass)
        self.assertEqual(0, len(e))
    
    def __GetXmlFromBookHandlerForBookWithAllFormats(self):
        return etree.fromstring(self.__handler.Handle("1"))
    
    def __GetXmlFromBookHandlerForBookWithNoFormats(self):
        return etree.fromstring(self.__handler.Handle("2"))
