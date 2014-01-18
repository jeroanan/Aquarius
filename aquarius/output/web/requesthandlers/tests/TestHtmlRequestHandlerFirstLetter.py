import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter import HtmlRequestHandlerFirstLetter


class TestHtmlRequestHandlerFirstLetter(unittest.TestCase):
    """Unit tests for the HtmlRequestHandlerFirstLetter class"""
    def setUp(self):
        """Common setup operations"""
        self.__a = Aquarius("hardcoded", None, None)
        self.__h = HtmlRequestHandlerFirstLetter(self.__a)
            
    def testFirstLetterHandlerCallsApplication(self):
        """Given a call to the first letter handler's handle method,
        then call the application's first letter handler method"""
        self.__a.list_books_by_first_letter = Mock(return_value=[])
        self.__h.handle("t")
        self.assertTrue(self.__a.list_books_by_first_letter.called)
