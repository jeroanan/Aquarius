#!/usr/bin/python3

import unittest
from config import config

class Config_Tests(unittest.TestCase):
    
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
        self.assertTrue(hasattr(self.__c, "SqlLiteDatabasePath"))
        