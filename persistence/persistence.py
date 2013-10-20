class persistence(object):   
    
    def SearchBooks(self, searchTerm):
        raise NotImplementedError()
    
    def ListBooksByFirstLetter(self, firstLetter):
        raise NotImplementedError()
    
    def GetBookDetails(self, bookId):
        raise NotImplementedError()
