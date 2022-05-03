import os
from termutils import clear_terminal
from sys import argv

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
        if len(argv) == 4:
            if argv[2] == "new":
                f = open("./lists/" + argv[3] + ".txt", 'x')
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
    if len(argv) == 4:
        if argv[2] == "delete":
            #todo should delete if file is typed with .txt
            os.remove("./lists/" + argv[3] + ".txt")
            exit(0)

def main():
    #todo make all arguments to lowercase
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