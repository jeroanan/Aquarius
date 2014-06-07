import unittest
from aquarius.Persistence import Persistence


class MongoDbPersistence(Persistence):

    def get_book_by_title_and_author(self, book):
        pass


class TestMongoDbPersistence(unittest.TestCase):

    def test_instantiation(self):
        MongoDbPersistence()

    def test_is_persistence(self):
        target = MongoDbPersistence()
        self.assertIsInstance(target, Persistence)

    @unittest.skip("Need to add in MongoDb connection class/mocks")
    def test_get_book_by_title_and_author(self):
        target = MongoDbPersistence()
        target.get_book_by_title_and_author(None)
