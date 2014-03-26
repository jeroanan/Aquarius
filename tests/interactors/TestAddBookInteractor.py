import unittest
from unittest.mock import Mock
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestAddBookInteractor(unittest.TestCase):

    def test_execute(self):
        persistence = Mock(SqlitePersistence)
        o = AddBookInteractor(SqlitePersistence())
        o.execute(Book())