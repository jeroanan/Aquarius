import unittest
from unittest.mock import Mock

from aquarius.aquarius import aquarius
from aquarius.output.web.requesthandlers.htmlrequesthandlerfirstletter import htmlrequesthandlerfirstletter

class htmlrequesthandlerfirstletter_tests(unittest.TestCase):
    
    def setUp(self):
        self.__a = aquarius("hardcoded", None, None)
        self.__h = htmlrequesthandlerfirstletter(self.__a)
            
    def testFirstLetterHandlerCallsApplication(self):
        self.__a.ListBooksByFirstLetter = Mock(return_value=[])
        self.__h.Handle("t")
        self.assertTrue(self.__a.ListBooksByFirstLetter.called)
