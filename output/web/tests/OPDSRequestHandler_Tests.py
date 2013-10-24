from output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import unittest

class OPDSRequestHandler_Tests(unittest.TestCase):
    
    def setUp(self):
        self.__o = opdsrequesthandler()        
    
    def testIndexHandlerCheckFeedTag(self):
        x = self.__o.IndexHandler()
        self.assertEqual("feed", x.tag)
        self.assertEqual("http://www.w3.org/2005/Atom", x.attrib["xmlns"])
        self.assertEqual("http://opds-spec.org/2010/catalog", x.attrib["xmlns:opds"])
        self.assertEqual(len(x.findall('id')), 1)
        self.assertEqual(len(x.findall('title')), 1)
        self.assertEqual(x.findall('title')[0].text, "Aquarius EBook library")
        self.assertEqual(len(x.findall('link')), 1)
    
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
        
        