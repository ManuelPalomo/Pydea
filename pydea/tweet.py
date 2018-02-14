"""
This module contains all clases and functions used to store,
clean and manage Tweets

"""
import hashlib
import re


class Tweet:
    """
    Class that represents a tweet

    Attributes:
        id (int): Database unique id identificator
        hash (str): The original tweet text is hashed in order to be compared
        user (str): The user who wrote the tweet
        tweet (str): Tweet text
        timestamp (str): The date the tweet was written
    """

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
        """
        Initializes all attributes of the tweet with the arguments passed

        Args:
            hash (str): the hash string to be initialized
            user (str): username who wrote the tweet
            tweet (str): Tweet text
            timestamp (str): date when the tweet was written

        Returns:
            None
        """
        self.hash = hash
        self.user = user
        self.tweet = tweet
        self.timestamp = timestamp

    def initialize_from_tweet(self, user, tweet, timestamp):
        """
        Initializes the tweet attributes by providing the data that the twitter API provides

        Args:
            user (str): User wro wrote the tweet
            tweet (str): Twitter text (without filtering)
            timestamp (str): Self-explanatory

        Returns:
            None
        """
        def _hash_tweet(text):
            return hashlib.md5(str(text).encode()).hexdigest()

        def _tweet_cleanup(text):

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

        self.hash = _hash_tweet(tweet)
        self.user = user
        self.tweet = _tweet_cleanup(tweet)
        self.timestamp = timestamp
