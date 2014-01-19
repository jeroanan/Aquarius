class ParameterSanitiser(object):
    """Sanitises strings so they can be safely used as parameters
    in sql statements"""

    def sanitise(self, args):
        if args is None:
            return ()
        for arg in args:
            yield self.__sanitise_argument(arg)

    def __sanitise_argument(self, input_to_sanitise):
        """Sanitise the given input so that it can be used in
        sql statement parameters"""
        result = input_to_sanitise
        if result is None:
            result = ""
        result = self.__replace_single_quotes(result)
        return result

    @staticmethod
    def __replace_single_quotes(input_to_sanitise):
        """Replace any single quotes in the input string
        with two single quotes"""
        one_single_quote = "'"
        two_single_quotes = "''"
        print(str(input_to_sanitise).replace(one_single_quote, two_single_quotes))
        return str(input_to_sanitise).replace(one_single_quote, two_single_quotes)