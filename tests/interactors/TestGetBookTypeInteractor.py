import unittest
from unittest.mock import Mock
from aquarius.interactors.GetBookTypeInteractor import GetBookTypeInteractor
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestGetBookTypeInteractor(unittest.TestCase):

    def test_get_book_type_interactor(self):
        persistence = Mock(SqlitePersistence)
        target = GetBookTypeInteractor(persistence)
        target.execute("format_code")
        self.assertTrue(persistence.get_book_type.called)
