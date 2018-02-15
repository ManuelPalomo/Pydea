"""
This module contains all the database-related classes and
functions used to store and retrieve tweets
"""
import sqlite3
from tweet import Tweet
from config_parser import ConfigParser


class Database:
    def __init__(self, testmode):
        self.connection = None
        self.testmode = testmode
        self.database_name = ConfigParser.get_instance(
            "config.xml").database_name

    def connect(self):
        """
        Initializes the connection object by connecting the sqlite object to the
        database or memory depending on mode of operation
        """
        database_name = "pydea.db"
        if self.testmode:
            self.connection = sqlite3.connect(":memory:")
        else:
            self.connection = sqlite3.connect(database_name)

    def query(self, sql: str):
        """
        Performs a simple non parametrized query

        Args:
            sql (str): The query to be executed

        Returns:
            Cursor: A cursor with the executed query
        """
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

    def insert_tweet_safe_query(self, tweet):
        """
        Performs a insert parametrized query

        Args:
            tweet (Tweet): The tweet to be inserted

        Returns:
            None
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Tweet(hash, user, tweet, timestamp) VALUES(?,?,?,?)",
                       (tweet.hash, tweet.user, tweet.tweet, tweet.timestamp))


def initialize_database(database):
    """
    Initializes the needed tables for the operation of pydea

    Args:
        database(Database): Database to be initialized

    Returns:
        None
    """
    def _create_table_tweet(db):
        tweet_create_table_query = ('CREATE TABLE IF NOT EXISTS Tweet('
                                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                    'hash TEXT UNIQUE NOT NULL,'
                                    'user TEXT NOT NULL,'
                                    'tweet TEXT NOT NULL,'
                                    'timestamp DATETIME DEFAULT CURRENT_TIMESTAMP'
                                    'sent_to_remote INTEGER DEFAULT 0 '
                                    ');')
        index_query = "CREATE INDEX hash_index ON Tweet(hash);"
        db.query(tweet_create_table_query)
        db.query(index_query)

    _create_table_tweet(database)


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

    database.insert_tweet_safe_query(tweet)
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

    return _parse_query_to_tweet(row)


def get_latest_tweet(database):
    """
    Searches the database for the latest inserted tweet by date

    Args:
        database (Database): Database to be queried
    Returns:
        Tweet
    """
    select_query = "SELECT * FROM Tweet ORDER BY datetime(substr(timestamp,8,18)+substr(timestamp,25,29)) DESC LIMIT 1"
    cursor = database.query(select_query)
    row = cursor.fetchone()
    return _parse_query_to_tweet(row)


def _parse_query_to_tweet(row):
    user = row[1]
    tweet_hash = row[2]
    tweet = row[3]
    timestamp = row[4]

    retrieved_tweet = Tweet()
    retrieved_tweet.initialize_manually(user, tweet_hash, tweet, timestamp)
    print(retrieved_tweet.timestamp)
    return retrieved_tweet
