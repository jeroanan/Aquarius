from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class hardcodedharvester(object):
    
    def __init__(self, app, config):
        self.__app = app
    
    def doHarvest(self):
        self.__app.AddBook(self.__get_test_book())
        
    def __get_test_book(self):
        b = book()
        b.Author = "J. R. Hartley"
        b.Title = "Fly Fishing"
        b.Formats = [self.__get_test_format()]
        return b

    @staticmethod
    def __get_test_format():
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "/tmp/test.epub"
        return f
