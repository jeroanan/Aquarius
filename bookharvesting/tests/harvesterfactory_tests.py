from bookharvesting.hardcodedharvester import hardcodedharvester
from bookharvesting.harvesterfactory import harvesterfactory

import unittest

class harversterfactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = harvesterfactory()
        
    def testGetHardodedHarvester(self):
        h = self.__f.GetHarvester("something")
        self.assertIsInstance(h, hardcodedharvester)