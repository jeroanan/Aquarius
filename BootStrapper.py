#!/usr/bin/python3

from aquarius.Aquarius import Aquarius


class BootStrapper(object):

    def __init__(self):
        self.__a = Aquarius("sqlite", "web", "filesystem")

    def main(self):
        self.__a.main()

    def set_app(self, app):
        self.__a = app
              
if __name__=="__main__":
    BootStrapper().main()