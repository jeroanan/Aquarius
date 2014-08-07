import unittest
from unittest.mock import Mock
from aquarius.Aquarius import Aquarius
from aquarius.output.web.Web import WebServer
from aquarius.output.web.requesthandlers.RequestHandler import RequestHandler


class TestWebserver(unittest.TestCase):

    def setUp(self):
        self.__a = Aquarius(None, None, None)
        self.__r = Mock(RequestHandler)
        self.__w = WebServer(self.__a, self.__r)
        self.__w.get_user_agent = lambda: "test"

    def test_index_calls_request_handler(self):
        self.__w.index()
        self.assertTrue(self.__r.index_handler.called)

    def test_by_title_calls_request_handler(self):
        self.__w.bytitle()
        self.assertTrue(self.__r.by_title_handler.called)

    def test_first_letter_calls_request_handler(self):
        self.__w.firstletter("z")
        self.assertTrue(self.__r.first_letter_handler.called)

    def test_book_calls_request_handler(self):
        self.__w.book(1)
        self.assertTrue(self.__r.book_handler.called)

    def test_search_request_calls_request_handler(self):
        self.__w.search("search term")
        self.assertTrue(self.__r.search_handler.called)

    def test_harvest_calls_request_handler(self):
        self.__w.harvest()
        self.assertTrue(self.__r.harvest_handler.called)

