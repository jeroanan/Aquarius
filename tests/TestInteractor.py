import unittest
from aquarius.Interactor import Interactor


class TestInteractor(unittest.TestCase):

    def TestExecute(self):
        i = Interactor()
        i.execute("param")

