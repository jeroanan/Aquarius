from aquarius import aquarius
from bookharvesting.hardcodedharvester import hardcodedharvester

import unittest

class hardcodedharvester_tests(unittest.TestCase):
    
    def test_DoHarvest(self):
        h = hardcodedharvester(self.__app)
        h.DoHarvest()
        
        
    class __app(aquarius):
        
        def AddBook(self):
            pass