import unittest

from aquarius.output.web.Web import Web


class web_tests(unittest.TestSuite):
    
    @staticmethod
    def testCanInitialise():
        app = None
        config = None        
        Web(app, config)
