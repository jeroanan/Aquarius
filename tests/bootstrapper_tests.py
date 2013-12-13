#!/usr/bin/python3

import unittest
from bootstrapper import bootstrapper

class bootstrapper_tests(unittest.TestCase):
    
    def testCanInitialise(self):
        a = bootstrapper()