"""
This module contains all the database-related classes and
functions used to store and retrieve tweets

 TODO:
    *Move database_name to config.xml
"""
import sqlite3
from tweet import Tweet


class Database:
    def __init__(self, testmode):
        self.connection = None
        self.testmode = testmode

    def connect(self):
        database_name = "pydea.db"
        if self.testmode:
            self.connection = sqlite3.connect(":memory:")
        else:
            self.connection = sqlite3.connect(database_name)

    def query(self, sql: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        except(AttributeError, sqlite3.OperationalError):
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        return cursor


def initialize_database(database):
    """
    Initializes the needed tables for the operation of pydea

    Args:
        database(Database): Database to be initialized

    Returns:
        None
    """
    def create_table_tweet(db):
        tweet_create_table_query = ('CREATE TABLE IF NOT EXISTS Tweet('
                                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                    'hash TEXT UNIQUE NOT NULL,'
                                    'user TEXT NOT NULL,'
                                    'tweet TEXT NOT NULL,'
                                    'timestamp DATETIME DEFAULT CURRENT_TIMESTAMP'
                                    ')')
        index_query = "CREATE INDEX hash_index ON Tweet(hash)"
        db.query(tweet_create_table_query)
        db.query(index_query)

    create_table_tweet(database)


def insert_tweet(database, tweet):
    """
    Checks if the tweet hash exists, if not, inserts it

    Args:
        database (Database): Database in which the tweet has to be inserted
        tweet (Tweet): Tweet to be inserted

    Returns:
        bool: True if inserted, false if otherwise
    """
    check_if_exists_query = "SELECT * FROM Tweet WHERE hash = '{0}'".format(
        tweet.hash)

    cursor = database.query(check_if_exists_query)
    if len(cursor.fetchall()) != 0:
        return False

    insert_tweet_query = "INSERT INTO Tweet(hash, user, tweet, timestamp) VALUES('{0}','{1}','{2}','{3}')".format(
        tweet.hash, tweet.user, tweet.tweet, tweet.timestamp)
    database.query(insert_tweet_query)
    return True

def get_tweet(database, tweet_id):
    """
    Gets the tweet specified by the argument id

    Args:
        database (Database): Database in which the tweet has to be looked for
        tweet_id (int): id of the tweet to be retrieved

    Returns:
        Tweet: If exists, a tweet will be returned
    """
    select_query = "SELECT * FROM Tweet WHERE id = {0}".format(tweet_id)
    cursor = database.query(select_query)
    row = cursor.fetchone()

    user = row[1]
    tweet_hash = row[2]
    tweet = row[3]
    timestamp = row[4]

    retrieved_tweet = Tweet()
    retrieved_tweet.initialize_manually(user, tweet_hash, tweet, timestamp)
    return retrieved_tweet
