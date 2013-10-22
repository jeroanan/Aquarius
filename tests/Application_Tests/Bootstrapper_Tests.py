#!/usr/bin/python3

import unittest
from bootstrapper import bootstrapper

class Bootstrapper_Tests(unittest.TestCase):
    
    def testCanInitialise(self):
        a = bootstrapper()