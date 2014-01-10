import unittest

from aquarius.persistence.hardcodedpersistence.setuptestbookhelper import setuptestbookhelper


class setuptestbookhelper_tests(unittest.TestCase):
    
    def testDoSetup(self):
        h = setuptestbookhelper()
        books = h.Setup()
        self.assertEqual(2, len(books))