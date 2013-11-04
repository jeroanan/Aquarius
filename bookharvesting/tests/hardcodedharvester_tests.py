from bookharvesting.hardcodedharvester import hardcodedharvester
import unittest

class hardcodedharvester_tests(unittest.TestCase):
    
    def test_doharvest(self):
        h = hardcodedharvester()
        h.doharvest()