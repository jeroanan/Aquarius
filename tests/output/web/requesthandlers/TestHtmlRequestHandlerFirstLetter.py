from unittest.mock import Mock

from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter import HtmlRequestHandlerFirstLetter
from aquarius.output.web.requesthandlers.SearchTemplateHandler import SearchTemplateHandler
from tests.output.web.requesthandlers.RequestHandlerTestBase import RequestHandlerTestBase


class TestHtmlRequestHandlerFirstLetter(RequestHandlerTestBase):

    def setUp(self):
        self.initialise_app_mock()
        self.initialise_mock_search_template_handler()
        self.__h = HtmlRequestHandlerFirstLetter(self.app)
        self.__h.set_search_template_handler(self.__search_template_handler)

    def initialise_app_mock(self):
        RequestHandlerTestBase.initialise_app_mock(self)
        self.app.list_books_by_first_letter = Mock(return_value=[])

    def initialise_mock_search_template_handler(self):
        self.__search_template_handler = SearchTemplateHandler()
        self.__search_template_handler.render_search_template = Mock(return_value=None)
            
    def test_first_letter_handler_calls_application(self):
        self.__h.handle("t")
        self.assert_called(self.app.list_books_by_first_letter)

    def test_first_letter_handler_calls_search_template_handler(self):
        self.__h.handle("t")
        self.assert_called(self.__search_template_handler.render_search_template)
