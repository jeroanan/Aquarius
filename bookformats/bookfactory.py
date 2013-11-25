from bookformats.epub import epub

class bookfactory(object):
    
    def GetBook(self, filepath):        
        if filepath.lower().endswith(".epub"):
            return epub(filepath).Load()


