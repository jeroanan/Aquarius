#!/usr/bin/python3

import unittest
from output.console.console import console

class ConsoleOutput_Tests(unittest.TestCase):
        
    def testCanInitialise(self):
        app = None
        config = None
        
        c = console(app, config)
                       
if __name__=="__main__":
    unittest.main()