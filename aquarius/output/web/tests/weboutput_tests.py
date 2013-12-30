import unittest

from aquarius.output.web.web import web

class weboutput_tests(unittest.TestSuite):
    
    def testCanInitialise(self):
        app = None
        config = None        
        web(app, config)
        