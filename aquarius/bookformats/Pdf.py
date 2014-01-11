from PyPDF2 import PdfFileReader


class Pdf(object):

    def __init__(self, filename):
        self.__filename = filename
        self.__reader = None
        self.__author = ""
        self.__title = ""

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        self.__author = val

    @property
    def Title(self):
        return self.__title

    def Title(self, val):
        self.__title = val

    def set_pdf_reader(self, reader):
        self.__reader = reader

    def load(self):
        self.__reader = self.__get_reader()
        info = self.__reader.getDocumentInfo()
        self.author = info["/Author"]
        self.Title = info["/Title"]

    def __get_reader(self):
        if self.__reader is None:
            return PdfFileReader(open(self.__filename, "rb"))
        else:
            return self.__reader