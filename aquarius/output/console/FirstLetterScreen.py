from aquarius.output.console.ConsoleScreen import ConsoleScreen


class FirstLetterScreen(ConsoleScreen):

    def __init__(self, app):
        super().__init__(app)

    def main(self):
        print(self.get_strings().get_first_letter_string())
        s = self.input()
        result = self.get_app().list_books_by_first_letter(s)
        self.__first_letter_results(result)

    def __first_letter_results(self, results):
        print(self.get_strings().get_search_result_title_string())
        
        i = 0
        for result in results:
            i += 1
            print(result.title)
        print(self.get_strings().get_search_result_footer_string(i))

