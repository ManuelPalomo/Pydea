import hashlib
import re
import html.parser



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

    def initialize_from_tweet(self, user, tweet, timestamp):

        def hash_tweet(text):
            return hashlib.md5(str(text).encode()).hexdigest()

        def tweet_cleanup(text):
          #  cleaned_tweet = html.parser.HTMLParser().unescape(tweet)
            cleaned_tweet = str(text)
            cleaned_tweet = re.sub(
                r'[.,"!]+', '', cleaned_tweet, flags=re.MULTILINE)  # Punctuation marks
            cleaned_tweet = re.sub(
                r'^RT[\s]+', '', cleaned_tweet, flags=re.MULTILINE)  # Retweets
            cleaned_tweet = re.sub(
                r'https?:\/\/.*[\r\n]*', '', cleaned_tweet, flags=re.MULTILINE)  # Links
            cleaned_tweet = re.sub(
                r'^RT[\s]+', '', cleaned_tweet, flags=re.MULTILINE)  # Retweets

            cleaned_tweet = cleaned_tweet.lower()
            return cleaned_tweet

        self.hash = hash_tweet(tweet)
        self.user = user
        self.tweet = tweet_cleanup(tweet)
        self.timestamp = timestamp
