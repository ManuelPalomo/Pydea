"""
This module contains all clases and functions used to parse and process the configuration ini file
"""
from configparser import SafeConfigParser

"""
Singleton class that loads all the keys from config.ini, use get_instance for
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
        self.insertURL = None
        self._parse_config()

    def _parse_config(self):
        TWITTER_API = "twitter_API"
        DATABASE = "database"
        REMOTE = "remote"
        CONSUMER_KEY_TAG = "ConsumerKey"
        CONSUMER_SECRET_TAG = "ConsumerSecret"
        ACCESS_TOKEN_TAG = "AccessToken"
        ACCESS_TOKEN_SECRET_TAG = "AccessTokenSecret"
        DATABASE_NAME = "DatabaseName"
        INSERT_URL = "InsertURL"

        config = SafeConfigParser()
        config.read('config.ini')
        self.consumer_key = config.get(TWITTER_API, CONSUMER_KEY_TAG)
        self.consumer_secret = config.get(TWITTER_API, CONSUMER_SECRET_TAG)
        self.access_token = config.get(TWITTER_API, ACCESS_TOKEN_TAG)
        self.access_token_secret = config.get(
            TWITTER_API, ACCESS_TOKEN_SECRET_TAG)
        self.database_name = config.get(DATABASE, DATABASE_NAME)
        self.insertURL = config.get(REMOTE, INSERT_URL)
