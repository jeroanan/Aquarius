from pymongo import Connection
from tests.persistence.mongodbpersistence.Mocks.MongoCollectionMock import MongoCollectionMock


class MongoConnectionMock(Connection):

    def __init__(self, **kwargs):
        self.book = MongoCollectionMock(None, None)
