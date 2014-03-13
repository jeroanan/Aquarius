from zipfile import BadZipFile

from aquarius.bookformats.Epub import Epub
from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat


class EpubCreator(object):
    def create(self, filepath):
        b = None
        try:
            e = Epub(filepath)
            b = Book()
            self.__add_book_properties(b, e)
            self.__add_epub_format(filepath, b)
        except BadZipFile:
            pass
        except OSError:
            pass
        return b

    @staticmethod
    def __add_book_properties(b, epub):
        b.author = epub.author
        b.title = epub.title

    @staticmethod
    def __add_epub_format(filepath, b):
        bf = BookFormat()
        bf.Format = "EPUB"
        bf.Location = filepath
        b.formats = [bf]