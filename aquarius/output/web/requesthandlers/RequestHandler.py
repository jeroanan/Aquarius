from aquarius.output.web.requesthandlers.HtmlRequestHandler import HtmlRequestHandler
from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler

import xml.etree.ElementTree as etree


class RequestHandler(object):
    """Routes web request to the proper request object for mobile
    and opds requests"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app
        self.__htmlHandler = HtmlRequestHandler(app)
        self.__opdsHandler = OpdsRequestHandler(app)

    def index_handler(self, user_agent):
        """Handle requests for the index page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.index_handler())
        else:
            return self.__htmlHandler.index_handler()

    def by_title_handler(self, user_agent):
        """Handle requests for the list first letters page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.by_title_handler())

    def first_letter_handler(self, user_agent, first_letter):
        """Handle requests for the list books by first letter of title page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.first_letter_handler(first_letter))
        else:
            return self.__htmlHandler.first_letter_handler(first_letter)

    def book_handler(self, user_agent, book_id):
        """Handle requests for the book details page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.book_handler(book_id))
        else:
            return self.__htmlHandler.book_handler(book_id)

    def download_handler(self, user_agent, book_id, book_format):
        """Handle requests for book downloads"""
        if self.__is_opds_browser(user_agent):
            return self.__opdsHandler.download_handler(book_id, book_format)

    def search_handler(self, user_agent, search_term):
        """Handle requests for searches"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.search_handler(search_term))
        else:
            return self.__htmlHandler.search_handler(search_term)

    def harvest_handler(self):
        """Handle requests to harvest books"""
        return self.__htmlHandler.harvest_handler()

    def set_html_request_handler(self, handler):
        """Set the object used to handle html requests"""
        self.__htmlHandler = handler

    def set_opds_request_handler(self, handler):
        """Set the object used to handle opds requests"""
        self.__opdsHandler = handler

    @staticmethod
    def __is_opds_browser(user_agent):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return user_agent.find("Aldiko") > -1

    @staticmethod
    def __string_from_etree(in_string):
        return etree.tostring(in_string)
