#!/usr/bin/python3

import unittest
from output.outputfactory import outputfactory
from output.web.web import web
from output.console.console import console

class OutputFactory_Tests(unittest.TestCase):
    
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
        
if __name__=="__main__":
    unittest.main()