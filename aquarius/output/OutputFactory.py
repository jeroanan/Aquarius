from aquarius.output.console.Console import Console
from aquarius.output.dummy.Dummy import Dummy
from aquarius.output.web.Web import Web


class OutputFactory(object):
    """Makes an output object based on the type string that's passed in"""
    def __init__(self, app, config):
        """Set initial object state"""
        self.__app = app
        self.__config = config
        
    def get_output(self, output_type):
        """Get the correct output object based on the type string given"""
        if output_type == "web":
            return Web(self.__app, self.__config)
        elif output_type == "dummy":
            return Dummy()
        else:
            return Console(self.__app, self.__config)
