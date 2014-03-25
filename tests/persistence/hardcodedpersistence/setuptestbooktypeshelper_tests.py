import unittest

from aquarius.persistence.hardcodedpersistence.SetupTestBookTypesHelper import SetupTestBookTypesHelper


class TestSetupBookTypeHelper(unittest.TestCase):
    """Unit tests for the SetupTestBookTypesHelper class"""
    def testDoSetup(self):
        """Test that calling the setup function returns the
        correct number of book types"""
        h = SetupTestBookTypesHelper()
        types = h.setup()
        self.assertEqual(3, len(types))