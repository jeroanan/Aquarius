#!/usr/bin/python3

import unittest
from output.outputfactory import outputfactory

class OutputFactory_Tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = outputfactory(None)

    def testFactoryGivesConsoleOutputByDefault(self):
        self.__f.GetOutput("")
    
if __name__=="__main__":
    unittest.main()