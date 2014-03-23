import unittest

from aquarius.output.OutputFactory import OutputFactory
from aquarius.output.web.Web import Web
from aquarius.output.console.Console import Console


class TestOutputFactory(unittest.TestCase):

    def setUp(self):
        app = None
        config = None
        self.__f = OutputFactory(app, config)

    def test_factory_gives_console_output_by_default(self):
        o = self.__f.get_output("")
        self.assertIsInstance(o, Console)
        
    def test_get_web_output(self):
        o = self.__f.get_output("web")
        self.assertIsInstance(o, Web)
