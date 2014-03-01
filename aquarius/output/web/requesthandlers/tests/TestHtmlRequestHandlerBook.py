import unittest

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerBook import HtmlRequestHandlerBook


class TestHtmlRequestHandlerBook(unittest.TestCase):
    """Tests for the HtmlRequestHandlerBook class"""
    def setUp(self):
        """Common setup operations"""
        self.__testBookTitle = "The Book with no name"
        self.__testBookAuthor = "An Author"
        self.__handler = HtmlRequestHandlerBook(Aquarius("hardcoded", None, None))
        
    def testBookHandlerReturnsHtmlDocument(self):
        """Given a Handle call on the Book Handler,
        then return a html document"""
        self.__AssertIsHtmlDoc(self.__handler.handle("1"))

    def __AssertIsHtmlDoc(self, test_string):
        return self.assertTrue(test_string.startswith("<!DOCTYPE html>"))
