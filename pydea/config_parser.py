"""
This module contains all clases and functions used to parse and process the configuration xml file
"""
from xml.dom import minidom

"""
Singleton class that loads all the keys from config.xml, use get_instance for
instancing it
"""


class ConfigParser:
    """
    Gets the config.xml file and translates it to attributes

    Attributes
        filename (str): filename that has to be parsed
        consumer_key (str): Twitter apps key
        consumer_secret (str): Twitter apps key
        access_token (str): Twitter apps key
        access_token_secret (str): Twitter apps key
        database_name (str): How should the sqlite local database be named
        external_database_api_url (str):
    """
    __instance = None

    @staticmethod
    def get_instance(filename):
        """
        Singleton-kind way of obtaining a instance

        Args:
            filename(str): Filename to be parsed in order to initialize this class

        Returns:
            None
        """
        if ConfigParser.__instance is None:
            ConfigParser(filename)
        return ConfigParser.__instance

    def __init__(self, filename):
        if ConfigParser.__instance != None:
            raise Exception("This class is a singleton")
        else:
            ConfigParser.__instance = self

        self.filename = filename
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_token_secret = None
        self.database_name = None
        self.external_database_api_url = None
        self._parse_config()

    def _parse_config(self):
        CONSUMER_KEY_TAG = "ConsumerKey"
        CONSUMER_SECRET_TAG = "ConsumerSecret"
        ACCESS_TOKEN_TAG = "AccessToken"
        ACCESS_TOKEN_SECRET_TAG = "AccessTokenSecret"
        DATABASE_NAME = "DatabaseName"
        EXTERNAL_DATABASE_API = "ExternalDatabaseAPIURL"
        KEYS = "Key"

        keys_XML = minidom.parse(self.filename)
        keys = keys_XML.getElementsByTagName(KEYS)

        self.consumer_key = keys[0].attributes[CONSUMER_KEY_TAG].value
        self.consumer_secret = keys[1].attributes[CONSUMER_SECRET_TAG].value
        self.access_token = keys[2].attributes[ACCESS_TOKEN_TAG].value
        self.access_token_secret = keys[3].attributes[ACCESS_TOKEN_SECRET_TAG].value
        self.database_name = keys[4].attributes[DATABASE_NAME].value
        self.external_database_api_url = keys[5].attributes[EXTERNAL_DATABASE_API].value
