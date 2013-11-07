#!/usr/bin/python3

import unittest
from config import config

class config_tests(unittest.TestCase):
    
    def setUp(self):
        self.__c = config()

    def testWebServerAddressAttribute(self):
        addr = "localhost"
        self.__c.WebServerAddress = addr
        self.assertEqual(addr, self.__c.WebServerAddress)
        
    def testWebServerPortAttribute(self):
        port = 8080
        self.__c.WebServerPort = port
        self.assertEqual(port, self.__c.WebServerPort)
        
    def testSqliteDatabasePathAttribue(self):
        databasepath = "/tmp/test"
        self.__c.SqlLiteDatabasePath = databasepath
        self.assertEqual(databasepath, self.__c.SqlLiteDatabasePath)
    