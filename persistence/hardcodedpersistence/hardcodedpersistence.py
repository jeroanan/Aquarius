from persistence.persistence import persistence
from book import book
from bookformat import bookformat

class hardcodedpersistence(persistence):
    
    def __init__(self):
        self.__data = []
        b = book()
        b.Title = "book"
        b.Id = 1
        self.__data.append(b)
        
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "./1.EPUB"
        b.Formats.append(f)
        
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
            
    def GetBook(self, bookId):
        if bookId == 1:
            return "This is some book content"
        return None
