import unittest

from persistence.hardcodedpersistence.setuptestbookhelper import setuptestbookhelper

class setuptestbookhelper_tests(unittest.TestCase):
    
    def testDoSetup(self):
        h = setuptestbookhelper()
        books = h.Setup()
        self.assertEqual(1, len(books))