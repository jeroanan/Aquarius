#!/usr/bin/python3

import unittest
from BootStrapper import BootStrapper


class bootstrapper_tests(unittest.TestCase):
    
    @staticmethod
    def testCanInitialise():
        a = BootStrapper()