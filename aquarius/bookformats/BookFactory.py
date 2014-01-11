from zipfile import BadZipFile

from aquarius.bookformats.epubcreator import EpubCreator
from aquarius.bookformats.pdfcreator import PdfCreator


class BookFactory(object):
    """The BookFactory returns a book object for any supported filepath
    that it receives."""
    def __init__(self):
        """Set default book creator objects"""
        self.__epubcreator = EpubCreator()
        self.__pdfcreator = PdfCreator()

    @property
    def epub_creator(self):
        """Get the current object used for creating book objects
        from .epub files."""
        return self.__epubcreator

    @epub_creator.setter
    def epub_creator(self, val):
        """Set the object to use for creating book objects from .epub files"""
        self.__epubcreator = val

    @property
    def pdf_creator(self):
        """Get the current object used for creating book objects
        from .pdf files."""
        return self.__pdfcreator

    @pdf_creator.setter
    def pdf_creator(self, val):
        """Set the object to use for creating book objects from .pdf files"""
        self.__pdfcreator = val

    def get_book(self, filepath):
        """The factory method. Delegate to the relevant book creation object
        based on filename extension. Return whatever that object returns."""
        b = None
        if filepath.lower().endswith(".epub"):
            b = self.__epubcreator.create(filepath)
        elif filepath.lower().endswith("pdf"):
            b = self.__pdfcreator.create(filepath)
        return b

