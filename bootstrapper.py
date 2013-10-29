#!/usr/bin/python3

from aquarius import aquarius

class bootstrapper(object):
    
    def main(self):
        a = aquarius("hardcoded", "web")
        a.Main()
              
if __name__=="__main__":
    bootstrapper().main()