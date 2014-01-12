import unittest
from unittest.mock import Mock

from aquarius.aquarius import aquarius
from aquarius.output.web.requesthandlers.htmlrequesthandlerfirstletter import htmlrequesthandlerfirstletter


class TestHtmlRequestHandlerFirstLetter(unittest.TestCase):
    """Unit tests for the HtmlRequestHandlerFirstLetter class"""
    def setUp(self):
        """Common setup operations"""
        self.__a = aquarius("hardcoded", None, None)
        self.__h = htmlrequesthandlerfirstletter(self.__a)
            
    def testFirstLetterHandlerCallsApplication(self):
        """Given a call to the first letter handler's handle method,
        then call the application's first letter handler method"""
        self.__a.ListBooksByFirstLetter = Mock(return_value=[])
        self.__h.Handle("t")
        self.assertTrue(self.__a.ListBooksByFirstLetter.called)
