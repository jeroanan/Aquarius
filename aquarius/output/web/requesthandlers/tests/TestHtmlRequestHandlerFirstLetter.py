import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter import HtmlRequestHandlerFirstLetter


class TestHtmlRequestHandlerFirstLetter(unittest.TestCase):

    def setUp(self):
        self.__a = Aquarius("hardcoded", None, None)
        self.__h = HtmlRequestHandlerFirstLetter(self.__a)
            
    def testFirstLetterHandlerCallsApplication(self):
        self.__a.list_books_by_first_letter = Mock(return_value=[])
        self.__h.handle("t")
        self.assertTrue(self.__a.list_books_by_first_letter.called)
