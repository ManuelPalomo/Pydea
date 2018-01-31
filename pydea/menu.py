"""
This module unifies all the operations that could be done with pydea

TODO:
    *Implement database_startup
    *Implement tweet_capture
"""
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
    pass


def tweet_capture():
    pass

MENU_ACTIONS = {
    'main': menu,
    '1': database_startup,
    '2': tweet_capture,
    '0': exit,
}
