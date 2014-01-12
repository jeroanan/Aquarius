from aquarius.output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler
from aquarius.output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler

import xml.etree.ElementTree as etree


class requesthandler(object):
    """Routes web request to the proper request object for mobile
    and opds requests"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app
        self.__htmlHandler = htmlrequesthandler(app)
        self.__opdsHandler = opdsrequesthandler(app)

    def IndexHandler(self, user_agent):
        """Handle requests for the index page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.IndexHandler())
        else:
            return self.__htmlHandler.IndexHandler()

    def ByTitleHandler(self, user_agent):
        """Handle requests for the list first letters page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.ByTitleHandler())

    def FirstLetterHandler(self, user_agent, first_letter):
        """Handle requests for the list books by first letter of title page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.FirstLetterHandler(first_letter))
        else:
            return self.__htmlHandler.FirstLetterHandler(first_letter)

    def BookHandler(self, user_agent, book_id):
        """Handle requests for the book details page"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.BookHandler(book_id))
        else:
            return self.__htmlHandler.BookHandler(book_id)

    def DownloadHandler(self, user_agent, book_id, book_format):
        """Handle requests for book downloads"""
        if self.__is_opds_browser(user_agent):
            return self.__opdsHandler.DownloadHandler(book_id, book_format)

    def Search(self, user_agent, search_term):
        """Handle requests for searches"""
        if self.__is_opds_browser(user_agent):
            return self.__string_from_etree(self.__opdsHandler.Search(search_term))
        else:
            return self.__htmlHandler.SearchHandler(search_term)

    def HarvestHandler(self):
        """Handle requests to harvest books"""
        return self.__htmlHandler.HarvestHandler()

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
