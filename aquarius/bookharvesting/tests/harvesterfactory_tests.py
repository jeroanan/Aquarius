from aquarius.bookharvesting.filesystemharvester import filesystemharvester
from aquarius.bookharvesting.hardcodedharvester import hardcodedharvester
from aquarius.bookharvesting.harvesterfactory import harvesterfactory

import unittest


class harversterfactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = harvesterfactory(None, None)
        
    def testGetHardcodedHarvester(self):
        h = self.__f.GetHarvester("moo")
        self.assertIsInstance(h, hardcodedharvester)

    def testGetFilesystemHarvester(self):
        h = self.__f.GetHarvester("filesystem")
        self.assertIsInstance(h, filesystemharvester)