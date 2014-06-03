import unittest
from unittest.mock import Mock
from aquarius.interactors.GetBookDetailsInteractor import GetBookDetailsInteractor
from aquarius.persistence.sqlitepersistence import SqlitePersistence


class TestGetBookDetailsInteractor(unittest.TestCase):

    def test_execute_calls_persistence(self):
        persistence = Mock(SqlitePersistence)
        persistence.get_book_details = Mock()
        target = GetBookDetailsInteractor(persistence)
        target.execute("book_id")
        self.assertTrue(persistence.get_book_details.called)