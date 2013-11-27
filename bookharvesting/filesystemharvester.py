import os
from bookformats.bookfactory import bookfactory

class filesystemharvester(object):    
    
    def __init__(self, app):
        self.__app = app
        
    def doHarvest(self, path):
        for (path, dirs, files) in os.walk(path):
            self.__getFilesFromPath(path, files)

    def __getFilesFromPath(self, path, files):
        if self.__pathContainsFiles(files):
            self.__AddBook(path, files)

    def __pathContainsFiles(self, files):
        return len(files)>0
    
    def __AddBook(self, path, files):
        for afile in files:
            book = bookfactory().GetBook("%s/%s" % (path, afile))            
            if book!=None:
                self.__app.AddBook(book)