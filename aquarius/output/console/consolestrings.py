class consolestrings(object):
    """Holds strings that are output by the console output module"""
    def GetMainMenu(self):
        """The string that's output for the main menu"""
        text = """Main Menu
=========
1. Search for books
2. List books starting with...
3. Perform Harvest
0. Exit
=========
Please enter option:"""        
        return text
    
    def GetSearchString(self):
        """The string that's output for the search prompt"""
        return "Search by book title: "
    
    def GetSearchResultTitleString(self):
        """The string that's output for the header of the search results"""
        return """
        
Search Results
=============="""
        
    def GetSearchResultFooterString(self, number_of_results):
        """The string that's output for the footer of the search results"""
        return """==============
%d result(s) found
        
        """ % number_of_results
        
    def GetFirstLetterString(self):
        """The string that's output for the first letter prompt"""
        return "Search for books beginning with: "
