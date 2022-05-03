from sys import platform
from os import system

def clear_terminal():
    if platform == "linux" or platform == "linux2":
        system('clear')        
    elif platform == "darwin":
        system('clear')
    elif platform == "win32":
        system('cls')