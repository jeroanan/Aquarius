#!/usr/bin/python3

import unittest
from Config import Config


class config_tests(unittest.TestCase):
    
    def setUp(self):
        self.__c = Config()

    def testWebServerAddressAttribute(self):
        addr = "localhost"
        self.__c.web_server_address = addr
        self.assertEqual(addr, self.__c.web_server_address)
        
    def testWebServerPortAttribute(self):
        port = 8080
        self.__c.web_server_port = port
        self.assertEqual(port, self.__c.web_server_port)
        
    def testSqliteDatabasePathAttribue(self):
        databasepath = "/tmp/test"
        self.__c.sqllite_database_path = databasepath
        self.assertEqual(databasepath, self.__c.sqllite_database_path)
    
    def testHarvestPathsAttribute(self):
        paths = []
        paths.append("/home/jeroanan/Downloads")
        paths.append("/home/jeroanan/Documents")
        self.__c.harvest_paths = paths
        self.assertEqual(2, len(self.__c.harvest_paths))