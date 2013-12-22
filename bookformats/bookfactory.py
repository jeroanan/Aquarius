from bookformats.epub import epub
from zipfile import BadZipFile

class bookfactory(object):
    
    def GetBook(self, filepath):
        book = None        
        if filepath.lower().endswith(".epub"):
            book = self.__loadEpub(filepath)
        return book

    def __loadEpub(self, filepath):
        book = None
        try:
            book = epub(filepath).Load()
        except BadZipFile:
            pass
        except OSError:
            pass
        return book