from unittest.mock import Mock
from aquarius.Interactor import Interactor
from aquarius.Persistence import Persistence
from aquarius.interactors.ListBooksByFirstLetterInteractor import ListBooksByFirstLetterInteractor
from tests.interactors.InteractorTestBase import InteractorTestBase


class TestListBooksByFirstLetterInteractor(InteractorTestBase):

    def setUp(self):
        self.__persistence = Mock(Persistence)
        self.__target = ListBooksByFirstLetterInteractor(self.__persistence)

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        first_letter = "T"
        self.__target.execute(first_letter)
        self.assert_called(self.__persistence.list_books_by_first_letter)