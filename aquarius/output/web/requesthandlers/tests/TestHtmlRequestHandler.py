import unittest
from unittest.mock import Mock

from aquarius.aquarius import aquarius
from aquarius.output.web.requesthandlers.htmlrequesthandler \
    import htmlrequesthandler
from aquarius.output.web.requesthandlers.tests.Mocks.HtmlRequestHandlerDelegateSpy \
    import HtmlRequestHandlerDelegateSpy


class TestHtmlRequestHandler(unittest.TestCase):
    """Tests for the HtmlRequestHandler class"""
    def setUp(self):
        """Common setup operations"""
        self.__a = aquarius("hardcoded", None, None)
        self.__a.HarvestBooks = Mock(return_value=None)
        self.__spy = HtmlRequestHandlerDelegateSpy()
        self.__h = htmlrequesthandler(self.__a)
        
    def testIndexHandlerReturnsHtmlDocument(self):
        """Given a request for the index page, then return a html document"""
        self.__AssertIsHtmlDoc(self.__h.IndexHandler())

    def testSearchHandlerCallsSearchHandlerObject(self):
        """Given a request for a search, then the search handler object is called"""
        self.__h.set_search_handler(self.__spy)
        self.__h.SearchHandler("searchTerm")
        self.assertTrue(self.__spy.handle_called)

    def testHarvestHandlerCallsHarvestBooks(self):
        """Given a request to harvest books, then call the harvester method"""
        self.__h.HarvestHandler()
        self.assertTrue(self.__a.HarvestBooks.called)        

    def testBookHandlerCallsBookHandlerObject(self):
        """Given a request for book details, then the book details
        handler object is called"""
        self.__h.set_book_handler(self.__spy)
        self.__h.BookHandler("1")
        self.assertTrue(self.__spy.handle_called)
    
    def testDownloadHandlerReturnsSomething(self):
        """Given a download request, then download the file"""
        b = self.__h.DownloadHandler("1", "EPUB")        
        self.assertGreater(len(b), 0)

    def testFirstLetterHandlerReturnsHtmlDocument(self):
        """Given a request to list books by first letter, then the first
        letter handler object is called."""
        self.__h.set_first_letter_handler(self.__spy)
        self.__h.FirstLetterHandler("T")
        self.assertTrue(self.__spy.handle_called)

    #TODO: Extract the below into a static of some sort
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertTrue(teststring.startswith("<!DOCTYPE html>"))

    def testCanSetFirstLetterHandler(self):
        self.__h.set_first_letter_handler(None)