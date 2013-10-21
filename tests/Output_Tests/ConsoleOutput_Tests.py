#!/usr/bin/python3

import unittest
from output.console.console import console

class ConsoleOutput_Tests(unittest.TestCase):
        
    def testMain(self):
        console().main()
            
if __name__=="__main__":
    unittest.main()