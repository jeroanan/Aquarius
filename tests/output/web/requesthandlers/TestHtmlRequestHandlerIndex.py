from aquarius.output.web.requesthandlers.HtmlRequestHandlerIndex import HtmlRequestHandlerIndex
from tests.output.web.requesthandlers.RequestHandlerTestBase import RequestHandlerTestBase


class TestHtmlRequestHandlerIndex(RequestHandlerTestBase):

    def test_can_instantiate(self):
        RequestHandlerTestBase.initialise_app_mock(self)
        HtmlRequestHandlerIndex(self.app)
