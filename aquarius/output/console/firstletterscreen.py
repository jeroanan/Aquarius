from aquarius.output.console.tests.ConsoleScreen import ConsoleScreen


class firstletterscreen(ConsoleScreen):
    
    def __init__(self, app):
        super().__init__(app)

    def Main(self):
        print(self.get_strings().GetFirstLetterString())
        s = self.input()
        result = self.get_app().ListBooksByFirstLetter(s)
        self.__first_letter_results(result)

    def __first_letter_results(self, results):
        print(self.get_strings().GetSearchResultTitleString())
        
        i = 0
        for result in results:
            i += 1
            print(result.Title)
        print(self.get_strings().GetSearchResultFooterString(i))

