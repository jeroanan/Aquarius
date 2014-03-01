#!/usr/bin/python3

import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from BootStrapper import BootStrapper


class bootstrapper_tests(unittest.TestCase):

    def setUp(self):
        self.initialise_mock_app()
        self.__boot = BootStrapper()
        self.__boot.set_app(self.__app)

    def initialise_mock_app(self):
        self.__app = Aquarius("hardcoded", None, None)
        self.__app.main = Mock(return_value=None)

    def test_calling_main_calls_main(self):
        self.__boot.set_app(self.__app)
        self.__boot.main()
        self.assertTrue(self.__app.main.called)
