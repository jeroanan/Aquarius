from PyPDF2 import PdfFileReader


class Pdf(object):
    """Loads metadata from Pdf files."""
    def __init__(self, filename):
        """Load metadata from a .pdf file. Set object state to that metadata"""
        self.__filename = filename
        self.__reader = None
        self.__author = ""
        self.__title = ""

    @property
    def author(self):
        """The author of the loaded book"""
        return self.__author

    @author.setter
    def author(self, val):
        """Set the author of the book"""
        self.__author = val

    @property
    def title(self):
        """The title of the loaded book"""
        return self.__title

    @title.setter
    def title(self, val):
        """Set the title of the book"""
        self.__title = val

    def set_pdf_reader(self, reader):
        """Set the object to use to read the pdf file"""
        self.__reader = reader

    def load(self):
        self.__load_metadata()

    def __load_metadata(self):
        self.__reader = self.__get_reader()
        info = self.__reader.getDocumentInfo()
        self.author = info["/Author"]
        self.title = info["/Title"]

    def __get_reader(self):
        """Gets the correct object to use for reading PDF files"""
        if self.__reader is None:
            return PdfFileReader(open(self.__filename, "rb"))
        else:
            return self.__reader