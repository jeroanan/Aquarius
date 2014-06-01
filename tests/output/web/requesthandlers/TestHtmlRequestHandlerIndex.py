import unittest

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerIndex import HtmlRequestHandlerIndex


class TestHtmlRequestHandlerIndex(unittest.TestCase):

    def test_can_instantiate(self):
        HtmlRequestHandlerIndex(Aquarius(None, None, None, None))
