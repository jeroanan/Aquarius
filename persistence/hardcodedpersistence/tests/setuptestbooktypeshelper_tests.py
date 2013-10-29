import unittest

from persistence.hardcodedpersistence.setuptestbooktypeshelper import setuptestbooktypeshelper

class setuptestbooktypehelper_tests(unittest.TestCase):
            
    def testDoSetup(self):
        h = setuptestbooktypeshelper()
        types = h.Setup()
        self.assertEqual(3, len(types))