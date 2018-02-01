"""
This module unifies all the operations that could be done with pydea

TODO:
    *Implement database_startup
    *Implement tweet_capture
"""
import os.path
from config_parser import ConfigParser
from tweet_db import Database, initialize_database

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


def menu():
    print(LOGO)
    print()
    print("Select the operation you want to perform")
    print("1:Database Startup")
    print("2.Tweet Capture")
    print("0.Quit")
    choice = input("State your choice: ")
    _execute_menu(choice)


def _execute_menu(choice):
    if choice == "":
        MENU_ACTIONS['main']()
    else:
        try:
            MENU_ACTIONS[choice]()
        except KeyError:
            print("Invalid selection, please try again")
            MENU_ACTIONS['main']()


def database_startup():
    config_parser = ConfigParser.get_instance("config.xml")
    if os.path.isfile(config_parser.database_name):
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


def tweet_capture():
    pass


MENU_ACTIONS = {
    'main': menu,
    '1': database_startup,
    '2': tweet_capture,
    '0': exit,
}
