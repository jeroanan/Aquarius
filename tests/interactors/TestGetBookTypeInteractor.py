from unittest.mock import Mock
from aquarius.Persistence import Persistence
from aquarius.interactors.GetBookTypeInteractor import GetBookTypeInteractor
from tests.interactors.InteractorTestBase import InteractorTestBase


class TestGetBookTypeInteractor(InteractorTestBase):

    def test_get_book_type_interactor(self):
        persistence = Mock(Persistence)
        target = GetBookTypeInteractor(persistence)
        target.execute("format_code")
        self.assert_called(persistence.get_book_type)
