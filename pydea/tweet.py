"""
This module contains all clases and functions used to store,
clean and manage Tweets

"""
import hashlib
import re


class Tweet:
    def __init__(self):
        self.id = None
        self.hash = None
        self.user = None
        self.tweet = None
        self.timestamp = None

    def __repr__(self):
        return "Hash: {0}, User: {1}, Tweet: {2}, Timestamp: {3}".format(self.hash, self.user,
                                                                         self.tweet, self.timestamp)

    def initialize_manually(self, hash, user, tweet, timestamp):
        self.hash = hash
        self.user = user
        self.tweet = tweet
        self.timestamp = timestamp

    def initialize_from_tweet(self, user, tweet, timestamp):

        def hash_tweet(text):
            return hashlib.md5(str(text).encode()).hexdigest()

        def tweet_cleanup(text):

            URL_PATTERN = re.compile(
                r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
            HASHTAG_PATTERN = re.compile(r'#\w*')
            MENTION_PATTERN = re.compile(r'@\w*')
            RESERVED_WORDS_PATTERN = re.compile(r'^(RT|FAV)')
            SMILEYS_PATTERN = re.compile(
                r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}", re.IGNORECASE)

            cleaned_tweet = URL_PATTERN.sub('', text)
            cleaned_tweet = HASHTAG_PATTERN.sub('', cleaned_tweet)
            cleaned_tweet = MENTION_PATTERN.sub('', cleaned_tweet)
            cleaned_tweet = RESERVED_WORDS_PATTERN.sub('', cleaned_tweet)
            cleaned_tweet = SMILEYS_PATTERN.sub('', cleaned_tweet)
            cleaned_tweet = cleaned_tweet.lower()
            return cleaned_tweet

        self.hash = hash_tweet(tweet)
        self.user = user
        self.tweet = tweet_cleanup(tweet)
        self.timestamp = timestamp
