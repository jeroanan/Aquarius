import unittest

from aquarius.output.dummy.Dummy import Dummy
from aquarius.output.OutputFactory import OutputFactory
from aquarius.output.web.Web import Web
from aquarius.output.console.Console import Console


class TestOutputFactory(unittest.TestCase):
    """Unit tests for the OutputFactory class"""
    def setUp(self):
        """Common setup operations"""
        app = None
        config = None
        self.__f = OutputFactory(app, config)

    def testFactoryGivesConsoleOutputByDefault(self):
        """Given a call to the OutputFactory, when the output name is
        unrecognised, then the console output module is returned."""
        o = self.__f.get_output("")
        self.assertIsInstance(o, Console)
        
    def testGetWebOutput(self):
        """Given a call to the OutputFactory, when the output name is web,
        the the web output module is returned."""
        o = self.__f.get_output("web")
        self.assertIsInstance(o, Web)
    
    def testGetDummyOutput(self):
        """Given a call to the OutputFactory, when the output name is dummy,
        then the dummy output module is returned"""
        o = self.__f.get_output("dummy")
        self.assertIsInstance(o, Dummy)
