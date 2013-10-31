import os
import sqlite3

class sqlitepersistence(object):
    
    def __init__(self, config):
        self.__config = config
        self.__createdb()
    
    def __createdb(self):
        pass