import unittest

from aquarius.output.dummy.dummy import dummy
from aquarius.output.outputfactory import outputfactory
from aquarius.output.web.web import web
from aquarius.output.console.console import console


class TestOutputFactory(unittest.TestCase):
    """Unit tests for the OutputFactory class"""
    def setUp(self):
        """Common setup operations"""
        app = None
        config = None
        self.__f = outputfactory(app, config)

    def testFactoryGivesConsoleOutputByDefault(self):
        """Given a call to the OutputFactory, when the output name is
        unrecognised, then the console output module is returned."""
        o = self.__f.GetOutput("")
        self.assertIsInstance(o, console)
        
    def testGetWebOutput(self):
        """Given a call to the OutputFactory, when the output name is web,
        the the web output module is returned."""
        o = self.__f.GetOutput("web")
        self.assertIsInstance(o, web)       
    
    def testGetDummyOutput(self):
        """Given a call to the OutputFactory, when the output name is dummy,
        then the dummy output module is returned"""
        o = self.__f.GetOutput("dummy")
        self.assertIsInstance(o, dummy)
