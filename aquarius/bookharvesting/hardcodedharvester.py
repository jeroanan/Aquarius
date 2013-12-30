from objects.book import book
from objects.bookformat import bookformat

class hardcodedharvester(object):
    
    def __init__(self, app, config):
        self.__app = app
    
    def doHarvest(self):
        self.__app.AddBook(self.__GetTestBook())        
        
    def __GetTestBook(self):
        b = book()
        b.Author = "J. R. Hartley"
        b.Title = "Fly Fishing"
        b.Formats = [self.__GetTestFormat()]
        return b

    def __GetTestFormat(self):
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "/tmp/test.epub"
        return f

        
    
    
