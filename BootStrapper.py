#!/usr/bin/python3

from aquarius.aquarius import aquarius


class BootStrapper(object):
    
    @staticmethod
    def main():
        a = aquarius("sqlite", "web", "filesystem")
        a.Main()
              
if __name__=="__main__":
    BootStrapper().main()