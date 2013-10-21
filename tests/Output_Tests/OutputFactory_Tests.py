#!/usr/bin/python3

import unittest
from output.outputfactory import outputfactory

class OutputFactory_Tests:
    
    def testCanInitialise(self):
        f = outputfactory()

    def testFactoryGivesConsoleOutputByDefault(self):
        f = outputfactory()
        o = f.GetOutput("")
    
if __name__=="__main__":
    unittest.main()