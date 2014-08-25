import os
import threading
from PyPDF2.utils import PdfReadError
from aquarius.Harvester import Harvester
from aquarius.bookformats.BookFactory import BookFactory


class FileSystemHarvester(Harvester):

    def __init__(self, app, config):
        self.__app = app
        self.__config = config

    def do_harvest(self):
        self.__app.is_harvesting = True
        self.__begin_harvest_thread()

    def __begin_harvest_thread(self):
        threading.Thread(target=self.__harvest_config_targets).start()

    def __harvest_config_targets(self):
        for target in self.__config.harvest_paths:
            self.__harvest_paths(target)
        self.harvesting_finished()

    def __harvest_paths(self, target):
        for (path, dirs, files) in os.walk(target):
            self.__get_files_from_path(path, files)

    def __get_files_from_path(self, path, files):
        if self.__path_contains_files(files):
            self.__try_to_add_book(path, files)

    @staticmethod
    def __path_contains_files(files):
        return len(files) > 0

    def __try_to_add_book(self, path, files):
        try:
            self.__add_books(files, path)
        except KeyError:
            pass
        except AssertionError:
            pass
        except TypeError:
            pass
        except PdfReadError:
            pass
        except ValueError:
            pass
        except Exception as e:
            if e.args[0] == "file has not been decrypted":
                pass
            else:
                self.__app.is_harvesting = False
                raise

    def __add_books(self, files, path):
        for f in files:
            self.__add_book(path, f)

    def __add_book(self, book_path, book_filename):
        book = BookFactory().get_book("%s/%s" % (book_path, book_filename))
        if book is not None:
            self.__app.add_book(book)

    def harvesting_finished(self):
        self.__app.is_harvesting = False