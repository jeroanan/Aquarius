from aquarius.output.console.ConsoleScreen import ConsoleScreen


class SearchScreen(ConsoleScreen):
    """Displays the console search results screen"""
    def __init__(self, app):
        super().__init__(app)

    def main(self):
        """Display the console search results screen"""
        s = self.input()
        results = self.get_app().SearchBooks(s)
        self.__search_results_screen(results)

    def __search_results_screen(self, results):
        print(self.get_strings().get_search_result_title_string())
        i = 0
        for result in results:
            i += 1
            print(result.title)
        print(self.get_strings().get_search_result_footer_string(i))
