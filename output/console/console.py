from output.console.consolestrings import consolestrings

class console(object):      
 
    def Main(self):
        self.__MainMenu()
    
    def __MainMenu(self):
        s = consolestrings()
        print(s.GetMainMenu())
        o = input()

    

    