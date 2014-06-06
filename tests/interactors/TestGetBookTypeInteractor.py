import unittest
from unittest.mock import Mock
from aquarius.Persistence import Persistence
from aquarius.interactors.GetBookTypeInteractor import GetBookTypeInteractor


class TestGetBookTypeInteractor(unittest.TestCase):

    def test_get_book_type_interactor(self):
        persistence = Mock(Persistence)
        target = GetBookTypeInteractor(persistence)
        target.execute("format_code")
        self.assertTrue(persistence.get_book_type.called)
