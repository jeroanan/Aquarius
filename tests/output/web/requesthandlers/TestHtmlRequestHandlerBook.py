from unittest.mock import Mock

from aquarius.objects.Book import Book
from aquarius.output.web.requesthandlers.HtmlRequestHandlerBook import HtmlRequestHandlerBook
from tests.output.web.requesthandlers.RequestHandlerTestBase import RequestHandlerTestBase


class TestHtmlRequestHandlerBook(RequestHandlerTestBase):

    def setUp(self):
        RequestHandlerTestBase.initialise_app_mock(self)
        self.app.get_book_details = Mock(return_value=(Book()))
        self.__book_handler = HtmlRequestHandlerBook(self.app)
        
    def test_book_handler_returns_html_document(self):
        self.__assert_is_html_doc(self.__book_handler.handle("1"))

    def __assert_is_html_doc(self, test_string):
        return self.assertTrue(test_string.startswith("<!DOCTYPE html>"))
