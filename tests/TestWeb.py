import unittest

from aquarius.output.web.Web import Web


class TestWeb(unittest.TestSuite):

    def test_can_initialise(self):
        app = None
        config = None        
        Web(app, config)
