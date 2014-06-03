import unittest
from aquarius.Aquarius import Aquarius


class RequestHandlerTestBase(unittest.TestCase):

    def initialise_app_mock(self):
        self.app = Aquarius(None, None, None, None)