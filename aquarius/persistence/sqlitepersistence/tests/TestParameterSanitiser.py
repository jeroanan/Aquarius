import unittest

from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class TestParameterSanitiser(unittest.TestCase):
    """Unit tests for the ParameterSanitiser class"""
    def setUp(self):
        """Common setup operations"""
        self.__sanitiser = ParameterSanitiser()

    """Unit tests for the ParameterSanitiser class"""
    def testSanitiseNone(self):
        """Given a null input, then return an empty string"""
        self.assertEqual("", self.__sanitiser.sanitise(None))

    def testSanitiseUnneeded(self):
        """Given a string, when no sanitising is necessary,
        return the same string"""
        self.assertEquals("moo", self.__sanitiser.sanitise("moo"))

    def testSanitiseQuotes(self):
        """Given a string, when the string contains quotes, then return a
        string with the quotes escaped"""
        self.assertEquals("''moo''", self.__sanitiser.sanitise("'moo'"))
