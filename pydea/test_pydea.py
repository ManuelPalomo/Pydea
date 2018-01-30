"""
Test module
"""
import unittest
from tweet import Tweet
from twitter_searcher import TwitterSearcher
from tweet_db import Database, initialize_database, insert_tweet, get_tweet


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

    def test_database_initialization_insertion_and_retrieval(self):
        db = Database(True)
        db.connect()
        initialize_database(db)

        cursor = db.query("SELECT name FROM sqlite_master WHERE type='table' AND name='Tweet'")
        self.assertTrue(cursor.rowcount != 0)

        test_tweet = Tweet()
        test_tweet.initialize_manually(
            "testhash123", "Test", "Test McTesterino", "29/01/2018")
        self.assertTrue(insert_tweet(db, test_tweet))

        retrieved_tweet = get_tweet(db, 1)
        self.assertIsNotNone(retrieved_tweet)

if __name__ == "__main__":
    unittest.main()
