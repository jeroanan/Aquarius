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
