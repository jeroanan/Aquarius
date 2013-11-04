from bookharvesting.hardcodedharvester import hardcodedharvester

class harvesterfactory(object):
    
    
    def GetHarvester(self, param1):
        return hardcodedharvester()
    
    
