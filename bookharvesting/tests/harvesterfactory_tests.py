from bookharvesting.hardcodedharvester import hardcodedharvester
from bookharvesting.harvesterfactory import harvesterfactory

import unittest

class harversterfactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = harvesterfactory(None, None)
        
    def testGetHardodedHarvester(self):
        h = self.__f.GetHarvester("moo")
        self.assertIsInstance(h, hardcodedharvester)