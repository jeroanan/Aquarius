from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class ParameterSanitiserSpy(ParameterSanitiser):
    def __init__(self):
        self.sanitise_calls = 0

    def sanitise(self, args):
        self.sanitise_calls += 1
        return args