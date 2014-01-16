#!/usr/bin/python3

from aquarius.Aquarius import Aquarius


class BootStrapper(object):
    
    @staticmethod
    def main():
        a = Aquarius("sqlite", "web", "filesystem")
        a.main()
              
if __name__=="__main__":
    BootStrapper().main()