#!/usr/bin/python3

from aquarius.objects.bookformat import bookformat

import unittest


class TestBookFormat(unittest.TestCase):
    """Unit tests for the BookFormat class"""
    def setUp(self):
        """Common setup operations"""
        self.format = bookformat()
        return format

    def testSetFormatAttribute(self):
        """Given a book format code, the object stores it."""
        self.format.Format = "Format"
        self.assertEqual("Format", self.format.Format)
        
    def testSetLocationAttribute(self):
        """Given a book location, the object stores it."""""
        self.format.Location = "/dev/null"
        self.assertEqual("/dev/null", self.format.Location)
        
    def testEqualityFormatsMatch(self):
        """Given another BookFormat object, given that format code and location
        are the same, then equality should evaluate to true."""
        f1 = self.__GetEPubFormat()
        f2 = self.__GetEPubFormat()
        self.assertTrue(f1 == f2)

    def testEqualityIsCaseInsensitive(self):
        """Given another BookFormat object, given that format code and location
        are the same but in different cases, then equality should evaluate
        to true."""
        f1 = self.__GetEPubFormat()
        f2 = self.__GetEPubFormat()
        f2.Format = str.lower(f2.Format)
        self.assertTrue(f1 == f2)

    def testEqualityFormatsDoNotMatch(self):
        """Given another BookFormat object, given that the format code/location
        are not the same, then equality should evaluate to false"""
        f1 = self.__GetEPubFormat()
        f2 = self.__GetPDFFormat()
        self.assertFalse(f1 == f2)
        
    def __GetEPubFormat(self):
        return self.__GetFormat("EPUB")

    def __GetPDFFormat(self):
        return self.__GetFormat("PDF")        
    
    @staticmethod
    def __GetFormat(formatcode):
        f2 = bookformat()
        f2.Format = formatcode
        return f2
