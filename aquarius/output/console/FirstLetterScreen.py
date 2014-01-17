from aquarius.output.console.ConsoleScreen import ConsoleScreen


class FirstLetterScreen(ConsoleScreen):
    """Displays all books beginning with the given letter"""
    def __init__(self, app):
        """Set initial object state"""
        super().__init__(app)

    def main(self):
        """Print the screen"""
        print(self.get_strings().get_first_letter_string())
        s = self.input()
        result = self.get_app().ListBooksByFirstLetter(s)
        self.__first_letter_results(result)

    def __first_letter_results(self, results):
        print(self.get_strings().get_search_result_title_string())
        
        i = 0
        for result in results:
            i += 1
            print(result.title)
        print(self.get_strings().get_search_result_footer_string(i))

