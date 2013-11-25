import unittest
import aquarius
from bookharvesting.filesystemharvester import filesystemharvester

class filesystemharvester_tests(unittest.TestCase):
    
    def setUp(self):
        self.__app = app()
        self.__h = filesystemharvester(self.__app)       
        
    def testHarvestSuccessful(self):
        self.__h.harvest("bookformats/tests/data/")
        self.assertEqual(1, len(self.__app.books))
        
class app(aquarius.aquarius):
    
    def __init__(self):
        self.books = []
    
    def AddBook(self, book):
        self.books.append(book)