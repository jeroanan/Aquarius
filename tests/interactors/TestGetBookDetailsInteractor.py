from unittest.mock import Mock
from aquarius.Persistence import Persistence
from aquarius.interactors.GetBookDetailsInteractor import GetBookDetailsInteractor
from tests.interactors.InteractorTestBase import InteractorTestBase


class TestGetBookDetailsInteractor(InteractorTestBase):

    def test_execute_calls_persistence(self):
        persistence = Mock(Persistence)
        persistence.get_book_details = Mock()
        target = GetBookDetailsInteractor(persistence)
        target.execute("book_id")
        self.assert_called(persistence.get_book_details)