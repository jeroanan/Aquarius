import os
from aquarius.bookformats.BookFactory import BookFactory


class FileSystemHarvester(object):
    """Harvest files book files from the given path in the filesystem"""
    def __init__(self, app, config):
        """Set initial object state"""
        self.__app = app
        self.__config = config

    def do_harvest(self):
        """Harvest the books from the filesystem"""
        for target in self.__config.harvest_paths:
            for (path, dirs, files) in os.walk(target):
                self.__get_files_from_path(path, files)

    def __get_files_from_path(self, path, files):
        if self.__path_contains_files(files):
            self.__add_book(path, files)

    @staticmethod
    def __path_contains_files(files):
        return len(files) > 0

    def __add_book(self, path, files):
        for f in files:
            book = BookFactory().get_book("%s/%s" % (path, f))
            if book is not None:
                self.__app.add_book(book)