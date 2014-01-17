class ConsoleStrings(object):
    """Holds strings that are output by the console output module"""

    @staticmethod
    def get_main_menu():
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
    
    def get_search_string(self):
        """The string that's output for the search prompt"""
        return "Search by book title: "
    
    def get_search_result_title_string(self):
        """The string that's output for the header of the search results"""
        return """
        
Search Results
=============="""
        
    def get_search_result_footer_string(self, number_of_results):
        """The string that's output for the footer of the search results"""
        return """==============
%d result(s) found
        
        """ % number_of_results
        
    def get_first_letter_string(self):
        """The string that's output for the first letter prompt"""
        return "Search for books beginning with: "
