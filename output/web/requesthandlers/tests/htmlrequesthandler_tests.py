

from aquarius import aquarius
from output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler

import unittest

class htmlrequesthandler_tests(unittest.TestCase):
    
    def setUp(self):
        self.h = htmlrequesthandler(aquarius("hardcoded", None, None))
        
    def testIndexHandler(self):
        self.__AssertIsHtmlDoc(self.h.IndexHandler())
        
    def testSearchHandler(self):
        self.__AssertIsHtmlDoc(self.h.SearchHandler("searchTerm"))
    
    def __AssertIsHtmlDoc(self, teststring):
        return self.assertEqual("<!DOCTYPE html>", str(teststring)[0:15])
