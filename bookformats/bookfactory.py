from bookformats.epub import epub
from zipfile import BadZipFile

class bookfactory(object):
    
    def GetBook(self, filepath):
        book = None        
        if filepath.lower().endswith(".epub"):
            try:
                book = epub(filepath).Load()
            except BadZipFile:
                pass
            except OSError:
                pass
        return book


