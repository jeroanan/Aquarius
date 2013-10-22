#!/usr/bin/python3

import unittest
from output.console.console import console

class ConsoleOutput_Tests(unittest.TestCase):
        
    def testCanInitialise(self):
        c = console()
                       
if __name__=="__main__":
    unittest.main()