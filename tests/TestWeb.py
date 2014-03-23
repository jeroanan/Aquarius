import unittest

from aquarius.output.web.Web import Web


class TestWeb(unittest.TestSuite):
    
    @staticmethod
    def testCanInitialise():
        app = None
        config = None        
        Web(app, config)
