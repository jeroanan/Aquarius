#!/usr/bin/python3

import unittest
from output.console.console import console
from output.output import output

class ConsoleOutput_Tests(unittest.TestCase):
        
    def testMain(self):
        console().main()
     
    def testIsOutput(self):
        c= console()         
        self.assertIsInstance(c, output)
                
if __name__=="__main__":
    unittest.main()