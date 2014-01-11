from aquarius.bookharvesting.filesystemharvester import filesystemharvester
from aquarius.bookharvesting.hardcodedharvester import hardcodedharvester
from aquarius.bookharvesting.harvesterfactory import harvesterfactory

import unittest


class TestHarvestFactory(unittest.TestCase):
    """Unit tests for the HarvestFactory class"""
    def setUp(self):
        self.__f = harvesterfactory(None, None)
        
    def testGetHardcodedHarvester(self):
        h = self.__f.GetHarvester("moo")
        self.assertIsInstance(h, hardcodedharvester)

    def testGetFilesystemHarvester(self):
        h = self.__f.GetHarvester("filesystem")
        self.assertIsInstance(h, filesystemharvester)