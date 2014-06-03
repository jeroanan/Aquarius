from unittest.mock import Mock

from aquarius.output.web.requesthandlers.HtmlRequestHandler \
    import HtmlRequestHandler
from aquarius.output.web.requesthandlers.HtmlRequestHandlerBook import HtmlRequestHandlerBook
from aquarius.output.web.requesthandlers.HtmlRequestHandlerDownload import HtmlRequestHandlerDownload
from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter import HtmlRequestHandlerFirstLetter
from aquarius.output.web.requesthandlers.HtmlRequestHandlerIndex import HtmlRequestHandlerIndex
from aquarius.output.web.requesthandlers.HtmlRequestHandlerSearch import HtmlRequestHandlerSearch
from tests.output.web.requesthandlers.RequestHandlerTestBase import RequestHandlerTestBase


class TestHtmlRequestHandler(RequestHandlerTestBase):

    def setUp(self):
        self.initialise_app_mock()
        self.initialise_search_handler_mock()
        self.initialise_book_handler_mock()
        self.initialise_first_letter_handler_mock()
        self.initialise_index_handler_mock()
        self.initialise_download_handler_mock()
        self.initialise_html_request_handler()

    def initialise_app_mock(self):
        RequestHandlerTestBase.initialise_app_mock(self)
        self.app.harvest_books = Mock(return_value=None)

    def initialise_search_handler_mock(self):
        self.__search_handler = HtmlRequestHandlerSearch(self.app)
        self.__search_handler.handle = Mock()

    def initialise_book_handler_mock(self):
        self.__book_handler = HtmlRequestHandlerBook(self.app)
        self.__book_handler.handle = Mock()

    def initialise_first_letter_handler_mock(self):
        self.__first_letter_handler = HtmlRequestHandlerFirstLetter(self.app)
        self.__first_letter_handler.handle = Mock()

    def initialise_index_handler_mock(self):
        self.__index_handler = HtmlRequestHandlerIndex(self.app)
        self.__index_handler.handle = Mock()

    def initialise_download_handler_mock(self):
        self.__download_handler = HtmlRequestHandlerDownload(self.app)
        self.__download_handler.handle = Mock()

    def initialise_html_request_handler(self):
        self.__h = HtmlRequestHandler(self.app)
        self.__h.set_search_handler(self.__search_handler)
        self.__h.set_book_handler(self.__book_handler)
        self.__h.set_first_letter_handler(self.__first_letter_handler)
        self.__h.set_index_handler(self.__index_handler)
        self.__h.set_download_handler(self.__download_handler)

    def test_search_handler_calls_search_handler_object(self):
        self.__h.search_handler("searchTerm")
        self.assertTrue(self.__search_handler.handle.called)

    def test_harvest_handler_calls_harvest_books(self):
        self.__h.harvest_handler()
        self.assertTrue(self.app.harvest_books.called)

    def test_book_handler_calls_book_handler_object(self):
        self.__h.book_handler("1")
        self.assertTrue(self.__book_handler.handle.called)

    def test_download_handler_calls_download_handler_object(self):
        self.__h.download_handler(None, None)
        self.assertTrue(self.__download_handler.handle.called)

    def test_first_letter_calls_first_letter_handler_object(self):
        self.__h.first_letter_handler("T")
        self.assertTrue(self.__first_letter_handler.handle.called)

    def test_index_calls_index_handler_object(self):
        self.__h.index_handler()
        self.assertTrue(self.__index_handler.handle.called)