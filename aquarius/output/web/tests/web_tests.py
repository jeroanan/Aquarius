import unittest

from aquarius.output.web.web import web

class web_tests(unittest.TestSuite):
    
    def testCanInitialise(self):
        app = None
        config = None        
        web(app, config)
        