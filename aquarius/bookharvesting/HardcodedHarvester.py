from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class HardcodedHarvester(object):
    """The hardcoded harvester. Just harvests some internally-held
    book objects."""
    def __init__(self, app, config):
        """Set up object state"""
        self.__app = app
    
    def do_harvest(self):
        """Do the harvest. Add resulting books to persistence"""
        self.__app.add_book(self.__get_test_book())
        
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
