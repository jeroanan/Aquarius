from persistence.persistence import persistence
from book import book

class hardcodedpersistor(persistence):
    
    def __init__(self):
        self.__data = []
        b = book()
        b.Title = "book"
        b.Id = 1
        self.__data.append(b)
        
    def SearchBooks(self, searchTerm):
        for book in self.__data:
            if searchTerm in book.Title and searchTerm != "":
                yield book
                
    def ListBooksByFirstLetter(self, firstLetter):
        for book in self.__data:
            if book.Title.startswith(firstLetter):
                yield book
                
    def GetBookDetails(self, bookId):
        for book in self.__data:
            if book.Id == bookId:
                return book
