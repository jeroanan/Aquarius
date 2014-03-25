import unittest

from aquarius.persistence.hardcodedpersistence.SetupTestBookHelper import SetupTestBookHelper


class TestSetupTestBookHelper(unittest.TestCase):

    def test_do_setup(self):
        h = SetupTestBookHelper()
        books = h.setup()
        self.assertEqual(2, len(books))