import unittest


class InteractorTestBase(unittest.TestCase):

    def assert_called(self, method):
        self.assertTrue(method.called)

    def assert_not_called(self, method):
        self.assertFalse(method.called)
