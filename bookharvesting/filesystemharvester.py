import os

class filesystemharvester(object):    
    
    def __init__(self, app):
        self.__app = app
        
    def harvest(self, path):
        for (path, dirs, files) in os.walk(path):
            self.__getFilesFromPath(path, files)    

    def __getFilesFromPath(self, path, files):
        if self.__pathContainsFiles(files):
            for afile in files:                
                self.__app.AddBook(afile)

    def __pathContainsFiles(self, files):
        return len(files)>0