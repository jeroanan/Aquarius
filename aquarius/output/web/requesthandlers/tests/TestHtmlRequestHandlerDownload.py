import unittest

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.HtmlRequestHandlerDownload import HtmlRequestHandlerDownload


class TestHtmlRequestHandlerDownload(unittest.TestCase):

    def test_can_initialise(self):
        HtmlRequestHandlerDownload(Aquarius("hardcoded", None, None))
