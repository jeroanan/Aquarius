from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler

import unittest


class opdsrequesthandler_tests(unittest.TestCase):
    
    def setUp(self):
        self.__o = OpdsRequestHandler(Aquarius("hardcoded", None, None))
        with open("./1.EPUB", 'w') as f:
            f.write("test\n")
        
    def checkCommonHeader(self, xmlDoc, expectedTitle):
        self.assertEqual("feed", xmlDoc.tag)
        self.assertEqual("http://www.w3.org/2005/Atom", xmlDoc.attrib["xmlns"])
        self.assertEqual("http://opds-spec.org/2010/catalog", xmlDoc.attrib["xmlns:opds"])
        self.assertEqual(len(xmlDoc.findall('id')), 1)
        self.assertEqual(len(xmlDoc.findall('title')), 1)
        self.assertEqual(xmlDoc.findall('title')[0].text, expectedTitle)
        self.assertEqual(len(xmlDoc.findall('link')), 1)
    
    def testIndexHandlerGivesTheCorrectFeedHeader(self):
        self.checkCommonHeader(self.__o.index_handler(), "Aquarius EBook library")
    
    def testIndexHandlerFeedTagContainsTheCorrectLinks(self):
        x = self.__o.index_handler()
        linkElement = x.findall('link')[0]
        self.assertEqual("/search/{searchTerms}", linkElement.attrib['href'])
        self.assertEqual("application/atom+xml", linkElement.attrib["type"])
        self.assertEqual("search", linkElement.attrib["rel"])
        self.assertEqual("Search", linkElement.attrib["title"])
        
    def testIndexHandlerContainsSomeEntries(self):
        x = self.__o.index_handler()
        self.assertGreater(len(x.findall('entry')), 0)
        
    def testIndexHandlerFirstEntryTitleIsBrowseByTitle(self):
        x = self.__o.index_handler().findall('entry')[0]
        self.assertEqual(len(x.findall('title')), 1)
        self.assertEqual(x.findall('title')[0].text, "List By Letter")
        
    def testIndexHandlerFirstEntryLinkIsCorrect(self):
        x = self.__o.index_handler().findall('entry')[0]
        self.assertEqual(len(x.findall('link')), 1)
        linkElement = x.findall("link")[0]
        self.assertEqual(linkElement.attrib["rel"], "subsection")
        self.assertEqual(linkElement.attrib["href"], "/bytitle")
        self.assertEqual(linkElement.attrib["type"], "application/atom+xml;profile=opds-catalog;kind=acquisition")
        
    def testIndexHandlerFirstEntryContainsIdElement(self):
        x = self.__o.index_handler().findall('entry')[0]
        self.assertEqual(len(x.findall("id")), 1)
        
    def testIndexHandlerFirstEntryContentTagIsCorrect(self):
        x = self.__o.index_handler().findall('entry')[0]
        self.assertEqual(len(x.findall("content")), 1)
        contentElement = x.findall("content")[0]
        self.assertEqual(contentElement.attrib["content"], "text")
        self.assertEqual("Browse books by title", contentElement.text)
        
    def testByTitleHandlerGivesTheCorrectFeedHeader(self):
        self.checkCommonHeader(self.__o.by_title_handler(), "Browse books by title")
        
    def testByTitleHandlerContainsTheCorrectNumberOfEntries(self):
        x = self.__o.by_title_handler()
        self.assertEqual(36, len(x.findall("entry")))
        
    def testFirstLetterHandlerGivesTheCorrectFeedHeader(self):
        self.checkCommonHeader(self.__o.first_letter_handler("0"), "Titles beginning with 0")
        
    def testFirstLetterHandlerReturnsNoBooksWhenItHasNone(self):
        x = self.__o.first_letter_handler("z")
        self.assertEqual(0, len(x.findall("entry")))        
    
    def testFirstLetterHandlerReturnsBooksWhenSomeStartingWithTheGivenLetterExist(self):
        x = self.__o.first_letter_handler("t")
        self.assertEqual(2, len(x.findall("entry")))
     
    def testFirstLetterGivesTheCorrectAuthorForABook(self):
        x = self.__o.first_letter_handler("t")
        self.assertEqual("An Author", x.findall("entry/content")[0].text)
        
    def testBookHandlerGivesTheCorrectFeedHeader(self):
        self.checkCommonHeader(self.__o.book_handler("1"), "Aquarius EBook Library")
        
    def testBookHandlerHasTheCorrectAcquisitionDetails(self):
        x = self.__o.book_handler("1")
        self.assertEqual(1, len(x.findall("entry")))

    def testBookHandlerHasTheCorrectAcqusitionLinks(self):
        x = self.__o.book_handler("1")
        self.assertEqual(3, len(x.findall("entry/link")))
    
    def testBookHandlerGivesTheCorrectAuthor(self):
        x = self.__o.book_handler("1")
        self.assertEqual("An Author", x.findall("entry/link/author/name")[0].text)
        self.assertEqual("about:none", x.findall("entry/link/author/uri")[0].text)
        
    def testDownloadGetsBook(self):
        x = self.__o.download_handler("1", "EPUB")
        self.assertNotEqual(None, x)        
        
    def testSearchGivesTheCorrectFeedHeader(self):
        x = self.__o.search_handler("oo")
        self.checkCommonHeader(x, "Search results for oo")
    
    def testSearchReturnsNoBooksWhenTheSearchQueryHasNoResults(self):
        x = self.__o.search_handler("sdkljsadjaskl")
        self.assertEqual(0, len(x.findall("entry")))
        
    def testSearchReturnsABookWhenTheSearchQueryHasAResult(self):
        x = self.__o.search_handler("oo")
        self.assertEqual(1, len(x.findall("entry")))
        