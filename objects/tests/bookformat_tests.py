#!/usr/bin/python3

from objects.bookformat import bookformat

import unittest

class bookformat_tests(unittest.TestCase):

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
        
    def testEqualityFormatsMatch(self):
        f1 = self.__GetEPubFormat()
        f2 = self.__GetEPubFormat()
        self.assertTrue(f1 == f2)

    def testEqualityFormatsDoNotMatch(self):
        f1 = self.__GetEPubFormat()
        f2 = self.__GetPDFFormat()
        self.assertFalse(f1 == f2)
        
    def __GetEPubFormat(self):
        return self.__GetFormat("EPUB")

    def __GetPDFFormat(self):
        return self.__GetFormat("PDF")        
    
    def __GetFormat(self, formatcode):
        f2 = bookformat()
        f2.Format = formatcode
        return f2
    
    

        