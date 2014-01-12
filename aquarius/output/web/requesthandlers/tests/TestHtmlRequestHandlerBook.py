import unittest
import xml.etree.ElementTree as etree

from aquarius.aquarius import aquarius
from aquarius.output.web.requesthandlers.htmlrequesthandlerbook import htmlrequesthandlerbook


class TestHtmlRequestHandlerBook(unittest.TestCase):
    """Tests for the HtmlRequestHandlerBook class"""
    def setUp(self):
        """Common setup operations"""
        self.__testBookTitle = "The Book with no name"
        self.__testBookAuthor = "An Author"
        self.__handler = htmlrequesthandlerbook(aquarius("hardcoded", None, None))
        
    def testBookHandlerReturnsHtmlDocument(self):
        """Given a Handle call on the Book Handler,
        then return a html document"""
        self.__AssertIsHtmlDoc(self.__handler.Handle("1"))

    #TODO: Extract the below into a static of some sort
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertEqual("<!DOCTYPE html>", str(teststring)[0:15])
