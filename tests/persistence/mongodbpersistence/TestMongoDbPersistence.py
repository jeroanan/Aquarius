import unittest
from pymongo import Connection
from pymongo.collection import Collection
from aquarius.Persistence import Persistence
from aquarius.objects.Book import Book


class MongoDbPersistence(Persistence):

    def __init__(self, connection):
        self.__connection = connection

    def get_book_by_title_and_author(self, book):
        result = self.__connection.book.find({"title": book.title, "author": book.author})
        b = Book()
        b.id = result["_id"]
        b.title = result["title"]
        b.author = result["author"]
        return b


class MongoCollectionMock(Collection):

    def __init__(self, database, name, **kwargs):
        self.__find_params = []
        self.__last_id = 0

    def find(self, *args, **kwargs):
        self.__find_params.append(args)
        ret_doc = {"_id": str(self.__get_id())}

        for k in args[0].keys():
            ret_doc[k] = args[0].get(k)

        return ret_doc

    def was_find_called_with_arg(self, arg):
        return self.__find_params.index((arg,)) > -1

    def __get_id(self):
        self.__last_id += 1
        return self.__last_id


class MongoConnectionMock(Connection):

    def __init__(self, **kwargs):
        self.book = MongoCollectionMock(None, None)


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


