from aquarius.objects.BookType import BookType


class SetupTestBookTypesHelper(object):
    """Add book types to the hardcoded persistence"""

    def __init__(self):
        self.__booktypes = []
               
    def setup(self):
        """Add book types to the hardcoded persistence"""
        self.__setup_epub_book_type()
        self.__setup_mobi_book_type()
        self.__setup_pdf_book_type()
        return self.__booktypes
    
    def __setup_epub_book_type(self):
        epub = BookType()
        epub.Format = "EPUB"
        epub.MimeType = "application/epub+zip"
        self.__booktypes.append(epub)
        
    def __setup_mobi_book_type(self):
        mobi = BookType()
        mobi.Format = "MOBI"
        mobi.MimeType = "application/x-mobipocket-ebook"
        self.__booktypes.append(mobi)
        
    def __setup_pdf_book_type(self):
        pdf = BookType()
        pdf.Format = "PDF"
        pdf.MimeType = "application/x-pdf"
        self.__booktypes.append(pdf)
    
    



