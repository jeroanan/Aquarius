class consolestrings(object):
    
    def GetMainMenu(self):
        text = """Main Menu
=========
1. Search for books
2. List books starting with...
=========
Please enter option:"""        
        return text
    
    def GetSearchString(self):
        return "Search by book title: "
    
    def GetSearchResultTitleString(self):
        return """
        
Search Results
=============="""
        
    def GetSearchResultFooterString(self, numberOfResults):
        return """==============
%d result(s) found
        
        """ % numberOfResults