"""
Main Module
"""
import sys
from menu import menu, console_execution


def main():
    if len(sys.argv) > 1:
        console_execution()
    else:
        menu()


if __name__ == "__main__":
    main()
