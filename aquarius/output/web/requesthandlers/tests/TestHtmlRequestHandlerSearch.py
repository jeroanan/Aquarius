import unittest

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerSearch import HtmlRequestHandlerSearch
from aquarius.output.web.requesthandlers.SearchTemplateHandler import SearchTemplateHandler


class TestHtmlRequestHandlerSearch(unittest.TestCase):

    def setUp(self):
        self.__app = AppSpy()
        self.__search_template_handler = SearchTemplateHandlerSpy()
        self.__h = HtmlRequestHandlerSearch(self.__app)
        self.__h.set_search_template_handler(self.__search_template_handler)

    def test_handle_calls_search(self):
        self.__h.handle("test")
        self.assertEquals(1, self.__app.search_books_called)

    def test_handle_calls_template_handler(self):
        self.__h.handle("test")
        self.assertEquals(1, self.__search_template_handler.render_search_template_called)

class AppSpy(Aquarius):

    def __init__(self):
        super(AppSpy, self).__init__("hardcoded", None, None)
        self.search_books_called = 0

    def search_books(self, searchterm):
        self.search_books_called += 1
        return []


class SearchTemplateHandlerSpy(SearchTemplateHandler):

    def __init__(self):
        self.render_search_template_called = 0

    def render_search_template(self, search_results):
        self.render_search_template_called += 1