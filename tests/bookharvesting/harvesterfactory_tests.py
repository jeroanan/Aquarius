from aquarius.bookharvesting.FileSystemHarvester import FileSystemHarvester
from aquarius.bookharvesting.HardcodedHarvester import HardcodedHarvester
from aquarius.bookharvesting.HarvesterFactory import HarvesterFactory

import unittest


class TestHarvestFactory(unittest.TestCase):

    def setUp(self):
        self.__f = HarvesterFactory(None, None)
        
    def test_get_hardcoded_harvest_returns_hardcoded_harvester(self):
        h = self.__f.get_harvester("moo")
        self.assertIsInstance(h, HardcodedHarvester)

    def test_get_filesystem_harvester_returns_filesystem_harvester(self):
        h = self.__f.get_harvester("filesystem")
        self.assertIsInstance(h, FileSystemHarvester)