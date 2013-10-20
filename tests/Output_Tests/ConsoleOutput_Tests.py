#!/usr/bin/python3

import unittest
from output.consoleoutput import consoleoutput

class ConsoleOutput_Tests(unittest.TestCase):
    
    def testCanInstantiate(self):
        o = consoleoutput()
            
if __name__=="__main__":
    unittest.main()