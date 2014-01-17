from aquarius.bookharvesting.FileSystemHarvester import FileSystemHarvester
from aquarius.bookharvesting.HardcodedHarvester import HardcodedHarvester
from aquarius.bookharvesting.HarvesterFactory import HarvesterFactory

import unittest


class TestHarvestFactory(unittest.TestCase):
    """Unit tests for the HarvestFactory class"""
    def setUp(self):
        self.__f = HarvesterFactory(None, None)
        
    def testGetHardcodedHarvester(self):
        """Given a harvester type, when the factory doesn't recognise it,
        then return the hardcoded harvester"""
        h = self.__f.get_harvester("moo")
        self.assertIsInstance(h, HardcodedHarvester)

    def testGetFilesystemHarvester(self):
        """Given a harvester type, when it's the filesystem harvester,
        return the filesystem harvester"""
        h = self.__f.get_harvester("filesystem")
        self.assertIsInstance(h, FileSystemHarvester)