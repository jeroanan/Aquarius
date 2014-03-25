import unittest
from Config import Config


class TestConfig(unittest.TestCase):
    
    def setUp(self):
        self.__c = Config()

    def test_set_webserver_stores_webserver(self):
        addr = "localhost"
        self.__c.web_server_address = addr
        self.assertEqual(addr, self.__c.web_server_address)
        
    def test_set_port_stores_port(self):
        port = 8080
        self.__c.web_server_port = port
        self.assertEqual(port, self.__c.web_server_port)
        
    def test_set_databasepath_stores_databasepath(self):
        databasepath = "/tmp/test"
        self.__c.sqllite_database_path = databasepath
        self.assertEqual(databasepath, self.__c.sqllite_database_path)
    
    def test_set_harvest_paths_stores_harvest_paths(self):
        paths = ["/home/jeroanan/Downloads", "/home/jeroanan/Documents"]
        self.__c.harvest_paths = paths
        self.assertEqual(2, len(self.__c.harvest_paths))