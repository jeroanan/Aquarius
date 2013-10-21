#!/usr/bin/python3

import unittest
from output.output import output

class  Output_Tests(unittest.TestCase):
    
    def setUp(self):
        self.o = output()
        
    def testMain(self):
        self.assertRaises(NotImplementedError, lambda: self.o.Main())
            
if __name__=="__main__":
    unittest.main()