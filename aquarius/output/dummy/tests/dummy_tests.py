import unittest
from aquarius.output.dummy.dummy import dummy


class dummy_tests(unittest.TestCase):
    """Unit tests for dummy output"""
    def testCanCallMain(self):
        """Given the dummy object, then main is a callable method"""
        dummy().Main()