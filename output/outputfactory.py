from output.console.console import console

class outputfactory(object):
    
    def GetOutput(self, outputtype):
        return console()
