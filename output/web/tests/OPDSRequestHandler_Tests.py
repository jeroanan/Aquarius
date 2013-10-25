from aquarius import aquarius
from output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import unittest

class OPDSRequestHandler_Tests(unittest.TestCase):
    
    def setUp(self):
        self.__o = opdsrequesthandler(aquarius("hardcoded", None))        
    
    def checkCommonHeader(self, xmlDoc, expectedTitle):
        self.assertEqual("feed", xmlDoc.tag)
        self.assertEqual("http://www.w3.org/2005/Atom", xmlDoc.attrib["xmlns"])
        self.assertEqual("http://opds-spec.org/2010/catalog", xmlDoc.attrib["xmlns:opds"])
        self.assertEqual(len(xmlDoc.findall('id')), 1)
        self.assertEqual(len(xmlDoc.findall('title')), 1)
        self.assertEqual(xmlDoc.findall('title')[0].text, expectedTitle)
        self.assertEqual(len(xmlDoc.findall('link')), 1)
    
    def testIndexHandlerCheckCommonHeader(self):
        self.checkCommonHeader(self.__o.IndexHandler(), "Aquarius EBook library")        
    
    def testIndexHandlerCheckFeedLinkTag(self):
        x = self.__o.IndexHandler()
        linkElement = x.findall('link')[0]
        self.assertEqual("/search/{searchTerms}", linkElement.attrib['href'])
        self.assertEqual("application/atom+xml", linkElement.attrib["type"])
        self.assertEqual("search", linkElement.attrib["rel"])
        self.assertEqual("Search", linkElement.attrib["title"])
        
    def testIndexHandlerContainsABunchOfEntries(self):
        x = self.__o.IndexHandler()
        self.assertGreater(len(x.findall('entry')), 0)
        
    def testIndexHandlerFirstEntryTitleIsBrowseByTitle(self):
        x = self.__o.IndexHandler().findall('entry')[0]
        self.assertEqual(len(x.findall('title')), 1)
        self.assertEqual(x.findall('title')[0].text, "List By Letter")
        
    def testIndexHandlerFirstEntryLink(self):
        x = self.__o.IndexHandler().findall('entry')[0]
        self.assertEqual(len(x.findall('link')), 1)
        linkElement = x.findall("link")[0]
        self.assertEqual(linkElement.attrib["rel"], "subsection")
        self.assertEqual(linkElement.attrib["href"], "/bytitle")
        self.assertEqual(linkElement.attrib["type"], "application/atom+xml;profile=opds-catalog;kind=acquisition")
        
    def testIndexHandlerFirstEntryContainsIdElement(self):
        x = self.__o.IndexHandler().findall('entry')[0]
        self.assertEqual(len(x.findall("id")), 1)
        
    def testIndexHandlerFirstEntryContentTag(self):
        x = self.__o.IndexHandler().findall('entry')[0]
        self.assertEqual(len(x.findall("content")), 1)
        contentElement = x.findall("content")[0]
        self.assertEqual(contentElement.attrib["content"], "text")
        self.assertEqual("Browse books by title", contentElement.text)
        
    def testByTitleHandlerCheckCommonHeader(self):
        self.checkCommonHeader(self.__o.ByTitleHandler(), "Browse books by title")
        
    def testByTitleHandlerContainsTheCorrectNumberOfEntries(self):
        x = self.__o.ByTitleHandler()        
        self.assertEqual(36, len(x.findall("entry")))        
        
    def testFirstLetterHandlerCheckCommonHeader(self):
        self.checkCommonHeader(self.__o.FirstLetterHandler("0"), "Titles beginning with 0")
        
    def testFirstLetterHandlerNoBooksForLetter(self):
        x = self.__o.FirstLetterHandler("z")
        self.assertEqual(0, len(x.findall("entry")))        
    
    def testFirstLetterHandlerBooksExistForLetter(self):
        x = self.__o.FirstLetterHandler("t")
        self.assertEqual(1, len(x.findall("entry")))
        