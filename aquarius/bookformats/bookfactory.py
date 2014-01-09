from zipfile import BadZipFile

from aquarius.bookformats.epubcreator import EpubCreator


class bookfactory(object):

    def __init__(self):
        self.__epubcreator = EpubCreator()

    @property
    def EpubCreator(self):
        return self.__epubcreator

    @EpubCreator.setter
    def EpubCreator(self, val):
        self.__epubcreator = val

    def GetBook(self, filepath):
        b = None
        if filepath.lower().endswith(".epub"):
            b = self.__epubcreator.create(filepath)
        return b

