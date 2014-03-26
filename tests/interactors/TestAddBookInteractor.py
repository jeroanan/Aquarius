import unittest
from unittest.mock import Mock
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestAddBookInteractor(unittest.TestCase):

    def test_execute_gets_book_from_persistence(self):
        persistence = Mock(SqlitePersistence)
        o = AddBookInteractor(persistence)
        o.execute(Book())
        self.assertTrue(persistence.get_book_by_title_and_author.called)