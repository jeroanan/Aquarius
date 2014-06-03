import unittest
from unittest.mock import Mock
from aquarius.Interactor import Interactor
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestAddBookInteractor(unittest.TestCase):

    def test_is_instance_of_interactor(self):
        target = AddBookInteractor(None)
        self.assertIsInstance(target, Interactor)

    def test_execute_gets_book_from_persistence(self):
        persistence = Mock(SqlitePersistence)
        persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book()))
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
        persistence = Mock(SqlitePersistence)
        persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book()))
        target = AddBookInteractor(persistence)
        target.execute(self.__get_book())
        self.assertFalse(persistence.add_book.called)

    def test_execute_with_format_adds_format(self):
        persistence = Mock(SqlitePersistence)
        persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book_with_format()))
        persistence.format_exists = Mock(return_value=False)
        target = AddBookInteractor(persistence)
        target.execute(self.__get_book_with_format())
        self.assertTrue(persistence.add_book_format.called)

    def test_execute_with_format_does_not_add_it_when_the_book_has_it(self):
        persistence = Mock(SqlitePersistence)
        persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book_with_format()))
        persistence.format_exists = Mock(return_value=True)
        target = AddBookInteractor(persistence)
        target.execute(self.__get_book_with_format())
        self.assertFalse(persistence.add_book_format.called)

    def __get_book_with_format(self):
        b = self.__get_book()
        bf = BookFormat()
        bf.Format = "EPUB"
        bf.Location = "/dev/null"
        b.add_format(bf)
        return b

    def __get_book(self):
        my_book = Book()
        my_book.id = 1337
        return my_book
