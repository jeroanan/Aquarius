import unittest

from aquarius.output.web.web import web


class web_tests(unittest.TestSuite):
    
    @staticmethod
    def testCanInitialise():
        app = None
        config = None        
        web(app, config)
