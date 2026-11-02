import shutil
import sys


commnads = [
    "exit",
    "echo",
    "type",
]

def main():

    while True:

        sys.stdout.write("$ ")
        command = input()


        parts = command.split()
        command = parts[0]
        args = parts[1:]


        if command == "exit" :
            break
        elif command == "echo" :
            print(" ".join(args))
        elif command == "type":
            runType(args[0])
        else :
            print(command + ": command not found")


def runType(command):

    if command in commnads :
        print(command + " is a shell builtin")

    else :

        loc = shutil.which(command)

        if loc != None:
            print(command + " is " + loc)

        else:
            print(command + ": not found")


if __name__ == "__main__":
    main()
