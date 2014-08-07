import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.Interactor import Interactor
from aquarius.InteractorFactory import InteractorFactory
from aquarius.bookharvesting.HardcodedHarvester import HardcodedHarvester
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.interactors.GetBookDetailsInteractor import GetBookDetailsInteractor
from aquarius.interactors.GetBookTypeInteractor import GetBookTypeInteractor
from aquarius.interactors.ListBooksByFirstLetterInteractor import ListBooksByFirstLetterInteractor
from aquarius.output.web.Web import Web
from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence


class TestAquarius(unittest.TestCase):
    
    def setUp(self):
        self.setup_interactors()
        self.__app = Aquarius("dummy", "whatever", self.__interactor_factory)
        self.__setup_harvester_mock()
        self.__gotCallback = False

    def setup_interactors(self):
        self.__search_book_interactor = Mock(Interactor)
        self.__add_book_interactor = Mock(AddBookInteractor)
        self.__list_books_by_first_letter_interactor = Mock(ListBooksByFirstLetterInteractor)
        self.__get_book_details_interactor = Mock(GetBookDetailsInteractor)
        self.__get_book_type_interactor = Mock(GetBookTypeInteractor)
        self.__interactor_factory = InteractorFactory()
        self.__interactor_factory.get_search_book_interactor = Mock(return_value=self.__search_book_interactor)
        self.__interactor_factory.get_add_book_interactor = Mock(return_value=self.__add_book_interactor)
        self.__interactor_factory.get_list_books_by_first_letter_interactor = \
            Mock(return_value=self.__list_books_by_first_letter_interactor)
        self.__interactor_factory.get_book_details_interactor = Mock(return_value=self.__get_book_details_interactor)
        self.__interactor_factory.get_book_type_interactor = Mock(return_value=self.__get_book_type_interactor)

    def __setup_harvester_mock(self):
        self.__harvester = harvester = HardcodedHarvester(self.__app, None)
        harvester.do_harvest = Mock()
        self.__app.set_harvester(harvester)

    def test_search_books_uses_interactor_factory(self):
        self.__app.search_books("")
        self.assertTrue(self.__interactor_factory.get_search_book_interactor.called)

    def test_search_books_calls_interactor(self):
        self.__app.search_books("")
        self.assertTrue(self.__search_book_interactor.execute.called)

    def test_list_books_by_first_letter_uses_interactor_factory(self):
        self.__app.list_books_by_first_letter("b")
        self.assertTrue(self.__interactor_factory.get_list_books_by_first_letter_interactor.called)

    def test_list_books_by_first_letter_calls_interactor(self):
        self.__app.list_books_by_first_letter("b")
        self.assertTrue(self.__list_books_by_first_letter_interactor.execute.called)

    def test_get_book_details_uses_interactor_factory(self):
        self.__app.get_book_details(0)
        self.assertTrue(self.__interactor_factory.get_book_details_interactor.called)

    def test_get_book_details_calls_interactor(self):
        self.__app.get_book_details(0)
        self.assertTrue(self.__get_book_details_interactor.execute.called)

    def test_get_book_type_uses_interactor_factory(self):
        self.__app.get_book_type("EPUB")
        self.assertTrue(self.__interactor_factory.get_book_type_interactor.called)

    def test_get_book_type_calls_interactor(self):
        self.__app.get_book_type("EPUB")
        self.assertTrue(self.__get_book_type_interactor.execute.called)

    def test_add_book_uses_interactor_factory(self):
        self.__app.add_book(None)
        self.assertTrue(self.__interactor_factory.get_add_book_interactor.called)

    def test_add_book_calls_interactor(self):
        self.__app.add_book(None)
        self.assertTrue(self.__add_book_interactor.execute.called)

    def test_call_main(self):
        output = Web(self.__app, None)
        output.main = Mock()
        self.__app.set_output(output)
        self.__app.main()
        self.assertTrue(output.main.called)

    def test_calling_harvest_books_calls_harvester(self):
        self.__app.harvest_books()
        self.assertTrue(self.__harvester.do_harvest.called)

    def test_calling_harvest_books_does_not_call_harvester_when_is_harvesting_set(self):
        self.__app.is_harvesting = True
        self.__app.harvest_books()
        self.assertFalse(self.__harvester.do_harvest.called)