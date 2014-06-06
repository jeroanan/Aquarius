import unittest
from unittest.mock import Mock
from aquarius.Persistence import Persistence
from aquarius.interactors.GetBookDetailsInteractor import GetBookDetailsInteractor


class TestGetBookDetailsInteractor(unittest.TestCase):

    def test_execute_calls_persistence(self):
        persistence = Mock(Persistence)
        persistence.get_book_details = Mock()
        target = GetBookDetailsInteractor(persistence)
        target.execute("book_id")
        self.assertTrue(persistence.get_book_details.called)