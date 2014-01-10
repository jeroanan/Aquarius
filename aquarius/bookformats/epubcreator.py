from zipfile import BadZipFile

from aquarius.bookformats.epub import epub
from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class EpubCreator(object):

    def create(self, filepath):
        b = None
        try:
            e = epub(filepath)
            b = book()
            self.__add_book_properties(b, e)
            self.__add_epub_format(filepath, b)
        except BadZipFile:
            pass
        except OSError:
            pass
        return b

    @staticmethod
    def __add_book_properties(b, epub):
        b.Author = epub.Author
        b.Title = epub.Title

    @staticmethod
    def __add_epub_format(filepath, b):
        bf = bookformat()
        bf.Format = "EPUB"
        bf.Location = filepath
        b.Formats = [bf]