from objects.book import book
from objects.bookformat import bookformat
from objects.booktype import booktype

class hardcodedpersistence():    

    def __init__(self):
        self.__data = []
        self.__booktypes = []
        
        self.SetupTestBook()        
        self.SetupBookTypes()       
        
    def SetupTestBook(self):
        b = book()
        b.Title = "The Book with no name"
        b.Id = 1
        self.__data.append(b)
        
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "./1.EPUB"
        b.Formats.append(f)
 
    def SetupBookTypes(self):
        self.SetupEpubBookType()
        self.SetupMobiBookType()
        self.SetupPdfBookType()
        
    def SetupEpubBookType(self):
        epub = booktype()
        epub.Format = "EPUB"
        epub.MimeType = "application/epub+zip"
        self.__booktypes.append(epub)
        
    def SetupMobiBookType(self):
        mobi = booktype()
        mobi.Format = "MOBI"
        mobi.MimeType = "application/x-mobipocket-ebook"
        self.__booktypes.append(mobi)
        
    def SetupPdfBookType(self):
        pdf = booktype()
        pdf.Format = "PDF"
        pdf.MimeType = "application/x-pdf"
        self.__booktypes.append(pdf)
        
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

    def GetBookType(self, formatcode):
        for bookType in self.__booktypes:
            if bookType.Format == formatcode:
                return bookType
            