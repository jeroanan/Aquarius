import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandler \
    import HtmlRequestHandler
from aquarius.output.web.requesthandlers.HtmlRequestHandlerBook import HtmlRequestHandlerBook
from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter import HtmlRequestHandlerFirstLetter
from aquarius.output.web.requesthandlers.HtmlRequestHandlerIndex import HtmlRequestHandlerIndex
from aquarius.output.web.requesthandlers.HtmlRequestHandlerSearch import HtmlRequestHandlerSearch


class TestHtmlRequestHandler(unittest.TestCase):

    def setUp(self):
        self.initialise_app_mock()
        self.initialise_search_handler_mock()
        self.initialise_book_handler_mock()
        self.initialise_first_letter_handler_mock()
        self.initialise_index_handler_mock()
        self.initialise_html_request_handler()

    def initialise_app_mock(self):
        self.__a = Aquarius("hardcoded", None, None)
        self.__a.harvest_books = Mock(return_value=None)

    def initialise_search_handler_mock(self):
        self.__search_handler = HtmlRequestHandlerSearch(self.__a)
        self.__search_handler.handle = Mock()

    def initialise_book_handler_mock(self):
        self.__book_handler = HtmlRequestHandlerBook(self.__a)
        self.__book_handler.handle = Mock()

    def initialise_first_letter_handler_mock(self):
        self.__first_letter_handler = HtmlRequestHandlerFirstLetter(self.__a)
        self.__first_letter_handler.handle = Mock()

    def initialise_index_handler_mock(self):
        self.__index_handler = HtmlRequestHandlerIndex(self.__a)
        self.__index_handler.handle = Mock()

    def initialise_html_request_handler(self):
        self.__h = HtmlRequestHandler(self.__a)
        self.__h.set_search_handler(self.__search_handler)
        self.__h.set_book_handler(self.__book_handler)
        self.__h.set_first_letter_handler(self.__first_letter_handler)
        self.__h.set_index_handler(self.__index_handler)

    def testSearchHandlerCallsSearchHandlerObject(self):
        self.__h.search_handler("searchTerm")
        self.assertTrue(self.__search_handler.handle.called)

    def testHarvestHandlerCallsHarvestBooks(self):
        self.__h.harvest_handler()
        self.assertTrue(self.__a.harvest_books.called)

    def testBookHandlerCallsBookHandlerObject(self):
        self.__h.book_handler("1")
        self.assertTrue(self.__book_handler.handle.called)
    
    def testDownloadHandlerReturnsSomething(self):
        b = self.__h.download_handler("1", "EPUB")
        self.assertGreater(len(b), 0)

    def testFirstLetterCallsFirstLetterHandlerObject(self):
        self.__h.first_letter_handler("T")
        self.assertTrue(self.__first_letter_handler.handle.called)

    def test_index_calls_index_handler_object(self):
        self.__h.index_handler()
        self.assertTrue(self.__index_handler.handle.called)