import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandler \
    import HtmlRequestHandler
from aquarius.output.web.requesthandlers.tests.Mocks.HtmlRequestHandlerDelegateSpy \
    import HtmlRequestHandlerDelegateSpy


class TestHtmlRequestHandler(unittest.TestCase):

    def setUp(self):
        self.__a = Aquarius("hardcoded", None, None)
        self.__a.harvest_books = Mock(return_value=None)
        self.__spy = HtmlRequestHandlerDelegateSpy()
        self.__h = HtmlRequestHandler(self.__a)
        
    def testIndexHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__h.index_handler())

    def testSearchHandlerCallsSearchHandlerObject(self):
        self.__h.set_search_handler(self.__spy)
        self.__h.search_handler("searchTerm")
        self.assertTrue(self.__spy.handle_called)

    def testHarvestHandlerCallsHarvestBooks(self):
        self.__h.harvest_handler()
        self.assertTrue(self.__a.harvest_books.called)

    def testBookHandlerCallsBookHandlerObject(self):
        self.__h.set_book_handler(self.__spy)
        self.__h.book_handler("1")
        self.assertTrue(self.__spy.handle_called)
    
    def testDownloadHandlerReturnsSomething(self):
        b = self.__h.download_handler("1", "EPUB")
        self.assertGreater(len(b), 0)

    def testFirstLetterHandlerReturnsHtmlDocument(self):
        self.__h.set_first_letter_handler(self.__spy)
        self.__h.first_letter_handler("T")
        self.assertTrue(self.__spy.handle_called)

    def __AssertIsHtmlDoc(self, test_string):
        return self.assertTrue(test_string.startswith("<!DOCTYPE html>"))

    def testCanSetFirstLetterHandler(self):
        self.__h.set_first_letter_handler(None)