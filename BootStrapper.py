#!/usr/bin/python3
from Config import Config

from aquarius.Aquarius import Aquarius
from aquarius.interactors.BasicInteractorFactory import BasicInteractorFactory
from aquarius.persistence.PersistenceFactory import PersistenceFactory


class BootStrapper(object):

    def __init__(self):
        persistence_type = "sqlite"
        output_type = "web"
        harvester_type = "filesystem"

        pf = PersistenceFactory(Config()).get_persistence(persistence_type)
        self.__a = Aquarius(persistence_type, output_type, harvester_type, BasicInteractorFactory(pf))

    def main(self):
        self.__a.main()

    def set_app(self, app):
        self.__a = app
              
if __name__ == "__main__":
    BootStrapper().main()