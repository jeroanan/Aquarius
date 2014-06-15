import unittest
from aquarius.Persistence import Persistence
from aquarius.objects.Book import Book
from aquarius.persistence.mongodbpersistence.MongoDbPersistence import MongoDbPersistence
from tests.persistence.mongodbpersistence.Mocks.MongoConnectionMock import MongoConnectionMock


class TestMongoDbPersistence(unittest.TestCase):

    def setUp(self):
        self.__mongo_conn = MongoConnectionMock()
        self.__book = Book()
        self.__book.title = "Treasure Island"
        self.__book.author = "Robert Louis Stevenson"
        self.__target = MongoDbPersistence(self.__mongo_conn)

    def test_is_persistence(self):
        self.assertIsInstance(self.__target, Persistence)

    def test_get_book_by_title_and_author_does_search(self):
        self.__target.get_book_by_title_and_author(self.__book)
        self.assertTrue(self.__mongo_conn.book.was_find_called_with_arg({
            "title": self.__book.title, "author": self.__book.author}))

    def test_search_book_by_title_and_author_returns_correct_object(self):
        actual_book = self.__target.get_book_by_title_and_author(self.__book)
        self.assertEqual(actual_book, self.__book)


