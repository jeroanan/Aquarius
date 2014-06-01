import unittest

from aquarius.Aquarius import Aquarius
from aquarius.bookharvesting.FileSystemHarvester import FileSystemHarvester
from Config import Config


class TestFileSystemHarvester(unittest.TestCase):

    def setUp(self):
        self.__app = App()
        config = Config()
        config.harvest_paths = ["aquarius/bookformats/tests/data"]
        self.__h = MyFileSystemHarvester(self.__app, config)

    def test_do_harvest_sets_harvest_flag_true_at_start_of_harvest(self):
        self.__h.do_harvest()
        self.assertTrue(self.__app.is_harvesting)


class MyFileSystemHarvester(FileSystemHarvester):

    def __init__(self, app, config):
        super().__init__(app, config)
        self.harvesting_finished_called = False

    def begin_harvest_thread(self):
        pass


class App(Aquarius):

    def __init__(self):
        super().__init__("hardcoded", None, None, None)
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)