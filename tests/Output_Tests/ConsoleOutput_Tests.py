#!/usr/bin/python3

import unittest
from output.console.consoleoutput import consoleoutput

class ConsoleOutput_Tests(unittest.TestCase):
        
    def testMain(self):
        consoleoutput().main()
            
if __name__=="__main__":
    unittest.main()