import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter import HtmlRequestHandlerFirstLetter
from aquarius.output.web.requesthandlers.SearchTemplateHandler import SearchTemplateHandler


class TestHtmlRequestHandlerFirstLetter(unittest.TestCase):

    def setUp(self):
        self.initialise_mock_app()
        self.initialise_mock_search_template_handler()
        self.__h = HtmlRequestHandlerFirstLetter(self.__a)
        self.__h.set_search_template_handler(self.__search_template_handler)

    def initialise_mock_app(self):
        self.__a = Aquarius(None, None, None, None)
        self.__a.list_books_by_first_letter = Mock(return_value=[])

    def initialise_mock_search_template_handler(self):
        self.__search_template_handler = SearchTemplateHandler()
        self.__search_template_handler.render_search_template = Mock(return_value=None)
            
    def test_first_letter_handler_calls_application(self):
        self.__h.handle("t")
        self.assertTrue(self.__a.list_books_by_first_letter.called)

    def test_first_letter_handler_calls_search_template_handler(self):
        self.__h.handle("t")
        self.assertTrue(self.__search_template_handler.render_search_template.called)
