import unittest
from tweet import Tweet
from twitter_searcher import TwitterSearcher
from tweet_db import Database, initialize_database, insert_tweet


class TestMethods(unittest.TestCase):

    def test_tweet_retrieval(self):
        twitter_searcher = TwitterSearcher()
        tweet_list = twitter_searcher.simple_search(1)

        retrieved_tweet = tweet_list[0]

        user = retrieved_tweet.user.name
        text = retrieved_tweet.text
        timestamp = retrieved_tweet.created_at

        tweet = Tweet()
        tweet.initialize_from_tweet(user, text, timestamp)
        self.assertTrue(tweet.user != None)
        self.assertTrue(tweet.tweet != None)

    def test_database(self):
        db = Database(True)
        initialize_database(db)

        test_tweet = Tweet()
        test_tweet.initialize_manually(
            "Test", "Test McTesterino", "29/01/2018")
        insert_tweet(db, test_tweet)


if __name__ == "__main__":
    unittest.main()
