import unittest

from aquarius.output.console.console import console

class console_tests(unittest.TestCase):
    
    def testCanInitialise(self):
        app = None
        config = None
        
        c = console(app, config)
        c.input = self.__testInput
        c.Main()
        
    def __testInput(self):
        return "0"
    
    def __testOutput(self, out):
        pass
