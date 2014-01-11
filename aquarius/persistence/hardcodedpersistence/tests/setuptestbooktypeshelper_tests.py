import unittest

from aquarius.persistence.hardcodedpersistence.SetupTestBookTypesHelper import SetupTestBookTypesHelper


class setuptestbooktypehelper_tests(unittest.TestCase):
            
    def testDoSetup(self):
        h = SetupTestBookTypesHelper()
        types = h.Setup()
        self.assertEqual(3, len(types))