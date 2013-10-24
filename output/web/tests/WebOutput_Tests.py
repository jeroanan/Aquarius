#!/usr/bin/python3

import unittest
from output.web.web import web

class WebOutput_Tests(unittest.TestSuite):
    
    def testCanInitialise(self):
        app = None
        config = None
        
        w = web(app, config)
        
if __name__=="__main__":
    unittest.main()