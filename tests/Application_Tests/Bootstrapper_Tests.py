#!/usr/bin/python3

import unittest
from bootstrapper import bootstrapper

class Bootstrapper_Tests(unittest.TestCase):
    
    def testMain(self):
        bootstrapper().main()