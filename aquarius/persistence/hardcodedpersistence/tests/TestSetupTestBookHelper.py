import unittest

from aquarius.persistence.hardcodedpersistence.SetupTestBookHelper import SetupTestBookHelper


class TestSetupTestBookHelper(unittest.TestCase):
    
    def testDoSetup(self):
        h = SetupTestBookHelper()
        books = h.Setup()
        self.assertEqual(2, len(books))