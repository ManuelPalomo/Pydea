"""
This module contains all clases and functions used to retrieve and query
Tweets from the Twitter API using python-twitter

"""
from xml.dom import minidom
import twitter


class TwitterSearcher:

    class TwitterKeys:
        def __init__(self):
            self.consumer_key = None
            self.consumer_secret = None
            self.access_token = None
            self.access_token_secret = None

        def parse_config_file(self, filename):
            CONSUMER_KEY_TAG = "ConsumerKey"
            CONSUMER_SECRET_TAG = "ConsumerSecret"
            ACCESS_TOKEN_TAG = "AccessToken"
            ACCESS_TOKEN_SECRET_TAG = "AccessTokenSecret"
            KEYS = "Key"

            keys_XML = minidom.parse(filename)
            keys = keys_XML.getElementsByTagName(KEYS)

            self.consumer_key = keys[0].attributes[CONSUMER_KEY_TAG].value
            self.consumer_secret = keys[1].attributes[CONSUMER_SECRET_TAG].value
            self.access_token = keys[2].attributes[ACCESS_TOKEN_TAG].value
            self.access_token_secret = keys[3].attributes[ACCESS_TOKEN_SECRET_TAG].value

    def __init__(self):
        self.twitter_keys = TwitterSearcher.TwitterKeys()
        self.twitter_keys.parse_config_file("config.xml")
        self.api = get_api(self.twitter_keys)

    def simple_search(self, number):
        return self.api.GetSearch(raw_query="q=should%20be%20an%20app&count={0}".format(number))

    def search_by_date(self, start_date, end_date):
        query = 'q=should%20be%20an%20app%20since%3A{0}%20until%3A{1}&count=100'.format(
            start_date, end_date)
        return self.api.GetSearch(raw_query=query)


def write_list_to_file(content_list, filename):
    file = open(filename, 'w')
    for element in content_list:
        file.write(str(element))
    file.close()


def get_api(twitter_keys):
    return twitter.Api(twitter_keys.consumer_key, twitter_keys.consumer_secret,
                       twitter_keys.access_token, twitter_keys.access_token_secret)
