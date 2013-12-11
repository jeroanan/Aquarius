from bookformats.epub import epub
from zipfile import BadZipFile

class bookfactory(object):
    
    def GetBook(self, filepath):
        book = None        
        if filepath.lower().endswith(".epub"):
            try:
                return epub(filepath).Load()
            except BadZipFile:
                pass
        return book


