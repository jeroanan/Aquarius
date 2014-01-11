import os
from aquarius.bookformats.BookFactory import BookFactory


class filesystemharvester(object):
    def __init__(self, app, config):
        self.__app = app
        self.__config = config

    def doHarvest(self):
        for target in self.__config.HarvestPaths:
            for (path, dirs, files) in os.walk(target):
                self.__get_files_from_path(path, files)

    def __get_files_from_path(self, path, files):
        if self.__path_contains_files(files):
            self.__add_book(path, files)

    @staticmethod
    def __path_contains_files(files):
        return len(files) > 0

    def __add_book(self, path, files):
        for afile in files:
            book = BookFactory().get_book("%s/%s" % (path, afile))
            if book is not None:
                self.__app.AddBook(book)