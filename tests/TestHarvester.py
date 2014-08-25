import unittest
from aquarius.Harvester import Harvester


class TestHarvester(unittest.TestCase):

    def setUp(self):
        self.__target = Harvester()

    def test_do_harvest(self):
        self.__assert_not_implemented(self.__target.do_harvest)

    def test_harvesting_finished(self):
        self.__assert_not_implemented(self.__target.harvesting_finished)

    def __assert_not_implemented(self, method):
        with self.assertRaises(NotImplementedError):
            method()