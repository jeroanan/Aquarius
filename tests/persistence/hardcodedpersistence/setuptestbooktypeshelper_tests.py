import unittest

from aquarius.persistence.hardcodedpersistence.SetupTestBookTypesHelper import SetupTestBookTypesHelper


class TestSetupBookTypeHelper(unittest.TestCase):

    def test_do_setup(self):
        h = SetupTestBookTypesHelper()
        types = h.setup()
        self.assertEqual(3, len(types))