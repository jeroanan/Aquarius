#!/usr/bin/python3

from aquarius.aquarius import aquarius

class bootstrapper(object):
    
    def main(self):
        a = aquarius("sqlite", "web", "filesystem")
        a.Main()
              
if __name__=="__main__":
    bootstrapper().main()