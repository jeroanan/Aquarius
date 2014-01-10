import unittest
from aquarius.output.dummy.dummy import dummy


class dummy_tests(unittest.TestCase):
        
    def testCanCallMain(self):
        dummy().Main()