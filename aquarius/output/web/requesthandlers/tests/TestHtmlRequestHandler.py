import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandler \
    import HtmlRequestHandler
from aquarius.output.web.requesthandlers.tests.Mocks.HtmlRequestHandlerDelegateSpy \
    import HtmlRequestHandlerDelegateSpy


class TestHtmlRequestHandler(unittest.TestCase):
    """Tests for the HtmlRequestHandler class"""
    def setUp(self):
        """Common setup operations"""
        self.__a = Aquarius("hardcoded", None, None)
        self.__a.HarvestBooks = Mock(return_value=None)
        self.__spy = HtmlRequestHandlerDelegateSpy()
        self.__h = HtmlRequestHandler(self.__a)
        
    def testIndexHandlerReturnsHtmlDocument(self):
        """Given a request for the index page, then return a html document"""
        self.__AssertIsHtmlDoc(self.__h.index_handler())

    def testSearchHandlerCallsSearchHandlerObject(self):
        """Given a request for a search, then the search handler object is called"""
        self.__h.set_search_handler(self.__spy)
        self.__h.search_handler("searchTerm")
        self.assertTrue(self.__spy.handle_called)

    def testHarvestHandlerCallsHarvestBooks(self):
        """Given a request to harvest books, then call the harvester method"""
        self.__h.harvest_handler()
        self.assertTrue(self.__a.HarvestBooks.called)        

    def testBookHandlerCallsBookHandlerObject(self):
        """Given a request for book details, then the book details
        handler object is called"""
        self.__h.set_book_handler(self.__spy)
        self.__h.book_handler("1")
        self.assertTrue(self.__spy.handle_called)
    
    def testDownloadHandlerReturnsSomething(self):
        """Given a download request, then download the file"""
        b = self.__h.download_handler("1", "EPUB")
        self.assertGreater(len(b), 0)

    def testFirstLetterHandlerReturnsHtmlDocument(self):
        """Given a request to list books by first letter, then the first
        letter handler object is called."""
        self.__h.set_first_letter_handler(self.__spy)
        self.__h.first_letter_handler("T")
        self.assertTrue(self.__spy.handle_called)

    #TODO: Extract the below into a static of some sort
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertTrue(teststring.startswith("<!DOCTYPE html>"))

    def testCanSetFirstLetterHandler(self):
        self.__h.set_first_letter_handler(None)