from aquarius.bookharvesting.FileSystemHarvester import FileSystemHarvester
from aquarius.bookharvesting.HarvesterFactory import HarvesterFactory

import unittest


class TestHarvestFactory(unittest.TestCase):

    def setUp(self):
        self.__f = HarvesterFactory(None, None)
        
    def test_get_filesystem_harvester_returns_filesystem_harvester(self):
        h = self.__f.get_harvester()
        self.assertIsInstance(h, FileSystemHarvester)