from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerSearch import HtmlRequestHandlerSearch
from aquarius.output.web.requesthandlers.SearchTemplateHandler import SearchTemplateHandler
from tests.output.web.requesthandlers.RequestHandlerTestBase import RequestHandlerTestBase


class TestHtmlRequestHandlerSearch(RequestHandlerTestBase):

    def setUp(self):
        self.initialise_app_mock()
        self.initialise_mock_search_template_handler()
        self.__h = HtmlRequestHandlerSearch(self.app)
        self.__h.set_search_template_handler(self.__search_template_handler)

    def initialise_mock_search_template_handler(self):
        self.__search_template_handler = SearchTemplateHandler()
        self.__search_template_handler.render_search_template = Mock(return_value=None)

    def initialise_app_mock(self):
        RequestHandlerTestBase.initialise_app_mock(self)
        self.app.search_books = Mock(return_value=[])

    def test_handle_calls_search(self):
        self.__h.handle("test")
        self.assertEquals(1, self.app.search_books.called)

    def test_handle_calls_template_handler(self):
        self.__h.handle("test")
        self.assertEquals(1, self.__search_template_handler.render_search_template.called)
