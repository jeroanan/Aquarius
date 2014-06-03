import unittest
from unittest.mock import Mock
from aquarius.Interactor import Interactor
from aquarius.interactors.SearchBookInteractor import SearchBookInteractor
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestSearchBookInteractor(unittest.TestCase):

    def test_is_instance_of_interactor(self):
        i = SearchBookInteractor(None)
        self.assertIsInstance(i, Interactor)

    def test_execute(self):
        persistence = Mock(SqlitePersistence)
        i = SearchBookInteractor(persistence)
        search_term = "Search Term"
        i.execute(search_term)

    def test_execute_calls_persistence(self):
        persistence = Mock(SqlitePersistence)
        i = SearchBookInteractor(persistence)
        search_term = "Search Term"
        i.execute(search_term)
        self.assertTrue(persistence.search_books.called)