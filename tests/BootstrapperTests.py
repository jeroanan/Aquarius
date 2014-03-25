import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from BootStrapper import BootStrapper


class BootstrapperTests(unittest.TestCase):

    def setUp(self):
        self.initialise_mock_app()
        self.__boot = BootStrapper()
        self.__boot.set_app(self.__app)

    def initialise_mock_app(self):
        self.__app = Aquarius(None, None, None)
        self.__app.main = Mock(return_value=None)

    @unittest.skip("This doesn't seem to be testable at the moment")
    def test_calling_main_calls_main(self):
        self.__boot.set_app(self.__app)
        self.__boot.main()
        self.assertTrue(self.__app.main.called)
