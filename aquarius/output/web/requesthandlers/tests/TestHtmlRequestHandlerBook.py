import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.output.web.requesthandlers.HtmlRequestHandlerBook import HtmlRequestHandlerBook


class TestHtmlRequestHandlerBook(unittest.TestCase):

    def setUp(self):
        self.__app = Aquarius("hardcoded", None, None)
        self.__app.get_book_details = Mock(return_value=(Book()))
        self.__book_handler = HtmlRequestHandlerBook(self.__app)
        
    def testBookHandlerReturnsHtmlDocument(self):
        self.__AssertIsHtmlDoc(self.__book_handler.handle("1"))

    def __AssertIsHtmlDoc(self, test_string):
        return self.assertTrue(test_string.startswith("<!DOCTYPE html>"))
