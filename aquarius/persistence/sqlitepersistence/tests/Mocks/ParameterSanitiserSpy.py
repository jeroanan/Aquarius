from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser


class ParameterSanitiserSpy(ParameterSanitiser):
    """Test double for ParameterSanitiser. Allows sensing of what
    gets called for that class when sql statements are being assembled"""
    def __init__(self):
        """Set initial object state"""
        self.sanitise_calls = 0

    def sanitise(self, args):
        """register that sanitise was called"""
        self.sanitise_calls += 1
        return args