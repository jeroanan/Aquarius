from aquarius.output.web.requesthandlers.HtmlRequestHandler import HtmlRequestHandler
from aquarius.output.web.requesthandlers.Jinja2Loader import Jinja2Loader
from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler

import xml.etree.ElementTree as etree


class RequestHandler(object):

    def __init__(self, app):
        self.__app = app
        self.__htmlHandler = HtmlRequestHandler(app)
        self.__opdsHandler = OpdsRequestHandler(app, Jinja2Loader())

    def index_handler(self, user_agent):
        if self.__is_opds_browser(user_agent):
            return self.__opdsHandler.index_handler()
        else:
            return self.__htmlHandler.index_handler()

    def by_title_handler(self, user_agent):
        if self.__is_opds_browser(user_agent):
            return self.__opdsHandler.by_title_handler()

    def first_letter_handler(self, user_agent, first_letter):
        if self.__is_opds_browser(user_agent):
            return self.__opdsHandler.first_letter_handler(first_letter)
        else:
            return self.__htmlHandler.first_letter_handler(first_letter)

    def book_handler(self, user_agent, book_id):
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.book_handler(book_id))
        else:
            return self.__htmlHandler.book_handler(book_id)

    def download_handler(self, user_agent, book_id, book_format):
        if self.__is_opds_browser(user_agent):
            return self.__opdsHandler.download_handler(book_id, book_format)

    def search_handler(self, user_agent, search_term):
        if self.__is_opds_browser(user_agent):
            return self.__opdsHandler.search_handler(search_term)
        else:
            return self.__htmlHandler.search_handler(search_term)

    def harvest_handler(self):
        return self.__htmlHandler.harvest_handler()

    def set_html_request_handler(self, handler):
        self.__htmlHandler = handler

    def set_opds_request_handler(self, handler):
        self.__opdsHandler = handler

    @staticmethod
    def __is_opds_browser(user_agent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return user_agent.find("Aldiko") > -1

    @staticmethod
    def __string_from_etree(in_string):
        return etree.tostring(in_string)
