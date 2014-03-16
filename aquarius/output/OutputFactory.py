from aquarius.output.console.Console import Console
from aquarius.output.web.Web import Web


class OutputFactory(object):

    def __init__(self, app, config):
        self.__app = app
        self.__config = config
        
    def get_output(self, output_type):
        if output_type == "web":
            return Web(self.__app, self.__config)
        else:
            return Console(self.__app, self.__config)
