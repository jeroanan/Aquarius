from book import book
from bookformat import bookformat

class hardcodedpersistence():
    
    def __init__(self):
        self.__data = []
        b = book()
        b.Title = "The Book with no name"
        b.Id = 1
        self.__data.append(b)
        
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "./1.EPUB"
        b.Formats.append(f)
        
    def SearchBooks(self, searchTerm):
        for book in self.__data:
            if str.upper(searchTerm) in str.upper(book.Title) and searchTerm != "":
                yield book
                
    def ListBooksByFirstLetter(self, firstLetter):
        for book in self.__data:
            if str.upper(book.Title).startswith(str.upper(firstLetter)):
                yield book
                
    def GetBookDetails(self, bookId):
        for book in self.__data:
            if book.Id == bookId:
                return book
            
    def GetBook(self, bookId):
        if bookId == 1:
            return "This is some book content"
        return None
