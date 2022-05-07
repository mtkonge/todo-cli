import os
from termutils import clear_terminal
from sys import argv
import re

commands = {
    "help": "shows all commands",
    "list new <name>": "creates a new list",
    "list all": "shows all list",
    "list edit <name>": "edits the specified list",
    "list delete <name>": "deletes a list"
}

def printCommands():
    for v in commands:
        print(v + ": " + commands[v])

def checkArgsAndCreateFile(argv: list[str]):
    amountOfDots = 0
    if len(argv) == 4:
        if argv[2] == "new":
            for i in range(len(argv[3])):
                if argv[3][i] == ".":
                    amountOfDots += 1
            if amountOfDots >= 2:
                print("More than one dot in the filename")
                exit(0)
            elif amountOfDots == 0:
                f = open("./lists/" + argv[3] + ".txt", "w+")
            if amountOfDots == 1 and re.search("\.txt$", argv[3]):
                f = open("./lists/" + argv[3], "w+")
            else:
                print("Invalid file syntax")
            exit(0)

def checkArgsAndShowFiles(argv: list[str]):
    if len(argv) == 3:
        if argv[2] == "all":
            for v in os.listdir("./lists"):
                print(v)
            exit(0)

def checkArgsAndEditFiles(argv: list[str]):
    if len(argv) == 4:
        if argv[2] == "edit":
            print("not implemented")
            exit(0)

def checkArgsAndDeleteFiles(argv: list[str]):
    amountOfDots = 0
    if len(argv) == 4:
        if argv[2] == "delete":
            for i in range(len(argv[3])):
                if argv[3][i] == ".":
                    amountOfDots += 1
            if amountOfDots >= 2:
                print("More than one dot in the filename")
                exit(0)
            elif amountOfDots == 0:
                os.remove("./lists/" + argv[3] + ".txt")
            if amountOfDots == 1 and re.search("\.txt$", argv[3]):
                os.remove("./lists/" + argv[3])
            else:
                print("Invalid file syntax") 
            
            exit(0)

def main():
    for i in range(len(argv)):
        argv[i] = argv[i].lower()
    if len(argv) == 1:
        print("Missing arguments")
        exit(0)
    if argv[1] == "help":
        printCommands()
        exit(0)
    elif argv[1] == "list":
        checkArgsAndCreateFile(argv)
        checkArgsAndShowFiles(argv)
        checkArgsAndEditFiles(argv)
        checkArgsAndDeleteFiles(argv)
    else:
        print("Invalid command")

if __name__=="__main__":
    main()