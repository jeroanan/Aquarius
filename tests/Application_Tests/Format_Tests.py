#!/usr/bin/python3

from bookformat import bookformat

import unittest

class Format_Tests(unittest.TestCase):

    def setUp(self):
        self.format = bookformat()
        return format

    def testHasFormatAttribute(self):
        self.assertEqual(True, hasattr(self.format, "Format"))
        
    def testHasLocationAttribute(self):
        self.assertEqual(True, hasattr(self.format, "Location"))
        
    def testSetFormatAttribute(self):
        self.format.Format = "Format"
        self.assertEqual("Format", self.format.Format)
        
    def testSetLocationAttribute(self):
        self.format.Location = "/dev/null"
        self.assertEqual("/dev/null", self.format.Location)