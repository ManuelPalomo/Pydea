"""
This module unifies all the operations that could be done with pydea

"""
import os.path
from config_parser import ConfigParser
from tweet_db import Database, initialize_database, insert_tweet, get_latest_tweet
from twitter_searcher import TwitterSearcher
from tweet import Tweet

LOGO = """

                          /$$        
                          | $$                    
  /$$$$$$  /$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$ 
 /$$__  $$| $$  | $$ /$$__  $$ /$$__  $$ |____  $$
| $$  \ $$| $$  | $$| $$  | $$| $$$$$$$$  /$$$$$$$
| $$  | $$| $$  | $$| $$  | $$| $$_____/ /$$__  $$
| $$$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$
| $$____/  \____  $$ \_______/ \_______/ \_______/
| $$       /$$  | $$                              
| $$      |  $$$$$$/                              
|__/       \______/ 
                             
by Manuel Palomo
 """
config_parser = ConfigParser.get_instance("config.xml")


def menu():
    print(LOGO)
    print()
    print("Select the operation you want to perform")
    print("1:Database Startup")
    print("2.Tweet Capture")
    print("3.Date Tweet Capture")
    print("0.Quit")
    choice = input("State your choice: ")
    _execute_menu(choice)


def console_execution():
    print(LOGO)
    print()
    print("Starting tweet capture")
    _tweet_capture(99)


def _execute_menu(choice):
    if choice == "":
        MENU_ACTIONS['main']()
    else:
        try:
            MENU_ACTIONS[choice]()
        except KeyError:
            print("Invalid selection, please try again")
            MENU_ACTIONS['main']()


def _database_startup():
    if _database_exists():
        print("{0} database already exists".format(
            config_parser.database_name))
        choice = input("Continue?(This will erase the database)(Y/N)")
        if choice.lower() != 'y':
            MENU_ACTIONS['main']()
        else:
            os.remove(config_parser.database_name)
            database = Database(False)
            initialize_database(database)
            print("Database initialized")
            MENU_ACTIONS['main']()
    else:
        database = Database(False)
        initialize_database(database)
        print("Database initialized")
        MENU_ACTIONS['main']()


def _database_exists():
    return os.path.isfile(config_parser.database_name)


def _tweet_capture(choice=-1):
    if not _database_exists():
        print("Database not initialized, run 'Database Startup' to continue")
        MENU_ACTIONS['main']()

    if choice == -1:
        choice = int(
            input("How many tweets do you want to capture?(99 max): "))

    if choice > 0 and choice <= 99:
        twitter_searcher = TwitterSearcher()
        tweet_list = twitter_searcher.simple_search(choice)
        database = Database(False)

        inserted_tweets = 0
        failed_tweets = 0
        for retrieved_tweet in tweet_list:
            if _save_tweet(retrieved_tweet, database):
                inserted_tweets += 1
            else:
                failed_tweets += 1
        print("{0} tweets inserted, {1} tweets were already in the database".format(
            inserted_tweets, failed_tweets))
    else:
        print("Error, wrong number")
        MENU_ACTIONS['main']()


def _date_tweet_capture():
    if not _database_exists():
        print("Database not initialized, run 'Database Startup' to continue")
        MENU_ACTIONS['main']()

    choice = int(input("How many tweets do you want to capture?(99 max): "))
    if choice > 0 and choice <= 99:
        twitter_searcher = TwitterSearcher()
        database = Database(False)
        tweet_list = twitter_searcher.search_by_date(
            choice, _get_last_tweet_date(database))

        inserted_tweets = 0
        failed_tweets = 0
        for retrieved_tweet in tweet_list:
            if _save_tweet(retrieved_tweet, database):
                inserted_tweets += 1
            else:
                failed_tweets += 1
        print("{0} tweets inserted, {1} tweets were already in the database".format(
            inserted_tweets, failed_tweets))
    else:
        print("Error, wrong number")
        MENU_ACTIONS['main']()


def _get_last_tweet_date(database):
    tweet = get_latest_tweet(database)
    return tweet.timestamp


def _save_tweet(retrieved_tweet, database):
    user = retrieved_tweet.user.name
    text = retrieved_tweet.full_text
    timestamp = retrieved_tweet.created_at

    tweet = Tweet()
    tweet.initialize_from_tweet(user, text, timestamp)
    return insert_tweet(database, tweet)


MENU_ACTIONS = {
    'main': menu,
    '1': _database_startup,
    '2': _tweet_capture,
    '3': _date_tweet_capture,
    '0': exit,
}
