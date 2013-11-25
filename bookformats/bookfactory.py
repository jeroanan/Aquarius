from objects.book import book
from bookformats.epub import epub

class bookfactory(object):
    
    def GetBook(self, filepath):        
        if filepath.endswith(".epub"):
            return epub(filepath).Load()


