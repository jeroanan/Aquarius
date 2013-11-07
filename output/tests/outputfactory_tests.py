#!/usr/bin/python3

import unittest

from output.dummy.dummy import dummy
from output.outputfactory import outputfactory
from output.web.web import web
from output.console.console import console

class outputfactory_tests(unittest.TestCase):
    
    def setUp(self):
        app = None
        config = None
        
        self.__f = outputfactory(app, config)

    def testFactoryGivesConsoleOutputByDefault(self):
        o = self.__f.GetOutput("")
        self.assertIsInstance(o, console)
        
    def testGetWebOutput(self):
        o = self.__f.GetOutput("web")
        self.assertIsInstance(o, web)       
    
    def testGetDummyOutput(self):
        o = self.__f.GetOutput("dummy")
        self.assertIsInstance(o, dummy)
        
if __name__=="__main__":
    unittest.main()