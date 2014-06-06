import unittest
from unittest.mock import Mock
from aquarius.Interactor import Interactor
from aquarius.Persistence import Persistence
from aquarius.interactors.ListBooksByFirstLetterInteractor import ListBooksByFirstLetterInteractor


class TestListBooksByFirstLetterInteractor(unittest.TestCase):

    def test_is_instance_of_interactor(self):
        i = ListBooksByFirstLetterInteractor(None)
        self.assertIsInstance(i, Interactor)

    def test_execute_calls_persistence(self):
        persistence = Mock(Persistence)
        i = ListBooksByFirstLetterInteractor(persistence)
        first_letter = "T"
        i.execute(first_letter)
        self.assertTrue(persistence.list_books_by_first_letter.called)
