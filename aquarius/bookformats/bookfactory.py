from zipfile import BadZipFile

from aquarius.bookformats.epubcreator import EpubCreator
from aquarius.bookformats.pdfcreator import PdfCreator


class bookfactory(object):

    def __init__(self):
        self.__epubcreator = EpubCreator()
        self.__pdfcreator = PdfCreator()

    @property
    def EpubCreator(self):
        return self.__epubcreator

    @EpubCreator.setter
    def EpubCreator(self, val):
        self.__epubcreator = val

    @property
    def PdfCreator(self):
        return self.__pdfcreator

    @PdfCreator.setter
    def PdfCreator(self, val):
        self.__pdfcreator = val

    def GetBook(self, filepath):
        b = None
        if filepath.lower().endswith(".epub"):
            b = self.__epubcreator.create(filepath)
        elif filepath.lower().endswith("pdf"):
            b = self.__pdfcreator.create(filepath)
        return b

