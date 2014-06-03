from aquarius.output.web.requesthandlers.HtmlRequestHandlerDownload import HtmlRequestHandlerDownload
from tests.output.web.requesthandlers.TestHtmlRequestHandler import TestHtmlRequestHandler


class TestHtmlRequestHandlerDownload(TestHtmlRequestHandler):

    def test_can_initialise(self):
        self.initialise_app_mock()
        HtmlRequestHandlerDownload(self.app)
