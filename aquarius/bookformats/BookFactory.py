from aquarius.bookformats.epubcreator import EpubCreator
from aquarius.bookformats.pdfcreator import PdfCreator


class BookFactory(object):
    def __init__(self):
        self.__epubcreator = EpubCreator()
        self.__pdfcreator = PdfCreator()

    @property
    def epub_creator(self):
        return self.__epubcreator

    @epub_creator.setter
    def epub_creator(self, val):
        self.__epubcreator = val

    @property
    def pdf_creator(self):
        return self.__pdfcreator

    @pdf_creator.setter
    def pdf_creator(self, val):
        self.__pdfcreator = val

    def get_book(self, filepath):
        b = None
        if filepath.lower().endswith(".epub"):
            b = self.__epubcreator.create(filepath)
        elif filepath.lower().endswith("pdf"):
            b = self.__pdfcreator.create(filepath)
        return b

