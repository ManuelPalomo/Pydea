"""
This module contains all clases and functions used to retrieve and query
Tweets from the Twitter API using python-twitter

"""
import twitter
from config_parser import ConfigParser


class TwitterSearcher:

    class TwitterKeys:
        def __init__(self):
            config_parser = ConfigParser.get_instance("config.xml")
            self.consumer_key = config_parser.consumer_key
            self.consumer_secret = config_parser.consumer_secret
            self.access_token = config_parser.access_token
            self.access_token_secret = config_parser.access_token_secret

    def __init__(self):
        self.twitter_keys = TwitterSearcher.TwitterKeys()
        self.api = get_api(self.twitter_keys)

    def simple_search(self, number):
        return self.api.GetSearch(raw_query="q=should%20be%20an%20app&count={0}".format(number))

    def search_by_date(self, number, start_date):
        query = "q=should%20be%20an%20app%20since%3A{0}&count={1}&src=typd".format(
            start_date, number)
        print(query)
        return self.api.GetSearch(raw_query=query)


def write_list_to_file(content_list, filename):
    file = open(filename, 'w')
    for element in content_list:
        file.write(str(element))
    file.close()


def get_api(twitter_keys):
    return twitter.Api(twitter_keys.consumer_key, twitter_keys.consumer_secret,
                       twitter_keys.access_token, twitter_keys.access_token_secret, tweet_mode='extended')
