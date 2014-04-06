import unittest
from unittest.mock import Mock
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestAddBookInteractor(unittest.TestCase):

    def test_execute_gets_book_from_persistence(self):
        persistence = Mock(SqlitePersistence)
        target = AddBookInteractor(persistence)
        target.execute(Book())
        self.assertTrue(persistence.get_book_by_title_and_author.called)

    def test_execute_with_new_book_adds_it(self):
        persistence = Mock(SqlitePersistence)
        persistence.get_book_by_title_and_author = Mock(return_value=Book())
        target = AddBookInteractor(persistence)
        target.execute(Book())
        self.assertTrue(persistence.add_book.called)

    def test_execute_with_existing_book_does_not_add_it(self):
        my_book = Book()
        my_book.id = 1337
        persistence = Mock(SqlitePersistence)
        persistence.get_book_by_title_and_author = Mock(return_value=my_book)
        target = AddBookInteractor(persistence)
        target.execute(my_book)
        self.assertFalse(persistence.add_book.called)
