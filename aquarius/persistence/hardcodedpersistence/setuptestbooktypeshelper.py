from objects.booktype import booktype

class setuptestbooktypeshelper(object):

    def __init__(self):
        self.__booktypes = []
               
    def Setup(self):
        self.__SetupEpubBookType()
        self.__SetupMobiBookType()
        self.__SetupPdfBookType()
        return self.__booktypes
    
    def __SetupEpubBookType(self):
        epub = booktype()
        epub.Format = "EPUB"
        epub.MimeType = "application/epub+zip"
        self.__booktypes.append(epub)
        
    def __SetupMobiBookType(self):
        mobi = booktype()
        mobi.Format = "MOBI"
        mobi.MimeType = "application/x-mobipocket-ebook"
        self.__booktypes.append(mobi)
        
    def __SetupPdfBookType(self):
        pdf = booktype()
        pdf.Format = "PDF"
        pdf.MimeType = "application/x-pdf"
        self.__booktypes.append(pdf)
    
    



