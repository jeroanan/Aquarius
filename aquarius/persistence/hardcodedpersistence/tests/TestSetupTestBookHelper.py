import unittest

from aquarius.persistence.hardcodedpersistence.SetupTestBookHelper import SetupTestBookHelper


class TestSetupTestBookHelper(unittest.TestCase):
    """Unit tests for the SetupTestBookHelper class"""
    def testDoSetup(self):
        """Given a call to the setup method, the correct books
        are returned"""
        h = SetupTestBookHelper()
        books = h.setup()
        self.assertEqual(2, len(books))