import unittest
from unittest.mock import Mock
from aquarius.Interactor import Interactor
from aquarius.Persistence import Persistence
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from tests.interactors.InteractorTestBase import InteractorTestBase


class TestAddBookInteractor(InteractorTestBase):

    def setUp(self):
        self.__persistence = Mock(Persistence)
        self.__target = AddBookInteractor(self.__persistence)

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_gets_book_from_persistence(self):
        self.__persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book()))
        self.__target.execute(Book())
        self.assertTrue(self.__persistence.get_book_by_title_and_author.called)

    def test_execute_with_new_book_adds_it(self):
        self.__persistence.get_book_by_title_and_author = Mock(return_value=Book())
        self.__target.execute(Book())
        self.assert_called(self.__persistence.add_book)

    def test_execute_with_existing_book_does_not_add_it(self):
        self.__persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book()))
        self.__target.execute(self.__get_book())
        self.assert_not_called(self.__persistence.add_book)

    def test_execute_with_format_adds_format(self):
        self.__persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book_with_format()))
        self.__persistence.format_exists = Mock(return_value=False)
        self.__target.execute(self.__get_book_with_format())
        self.assert_called(self.__persistence.add_book_format)

    def test_execute_with_format_does_not_add_it_when_the_book_has_it(self):
        self.__persistence.get_book_by_title_and_author = Mock(return_value=(self.__get_book_with_format()))
        self.__persistence.format_exists = Mock(return_value=True)
        self.__target.execute(self.__get_book_with_format())
        self.assert_not_called(self.__persistence.add_book_format)

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
