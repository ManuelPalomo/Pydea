import sqlite3


class Database:
    def __init__(self, testmode):
        self.connection = None
        self.testmode = testmode

    def connect(self):
        # TODO Move database_name to config.xml
        DATABASE_NAME = "pydea.db"
        if self.testmode:
            self.connection = sqlite3.connect(":memory:")
        else:
            self.connection = sqlite3.connect(DATABASE_NAME)

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
    def create_table_tweet(db):
        QUERY = "CREATE TABLE IF NOT EXISTS Tweet(id INTEGER PRIMARY KEY AUTOINCREMENT,hash TEXT NOT NULL,tweet TEXT NOT NULL,timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)"
        cursor = db.query(QUERY)

    create_table_tweet(database)


def insert_tweet(database, tweet):
    check_if_exists_query = "SELECT * FROM Tweet WHERE hash = {0}".format(
        tweet.hash)

    cursor = database.query(check_if_exists_query)
    if cursor.rowcount() != 0:
        return False

    insert_tweet_query = "INSERT INTO Tweet (hash, tweet, timestamp) VALUES({0},{1},{2})".format(
        tweet.hash, tweet.tweet, tweet.timestamp)

    database.query(insert_tweet_query)
    return True
