import os
import shutil
import subprocess
import sys



commnads = [
    "exit",
    "echo",
    "type",
]

def main():

    while True:

        sys.stdout.write("$ ")
        rawInput = input()


        parts = rawInput.split()
        command = parts[0]
        args = parts[1:]


        if command == "exit" :

#test this shit is gay is as fuck nigga
            break
        elif command == "echo" :
            print(" ".join(args))
        elif command == "type":
            runType(args[0])
        elif command == "pwd":
            print(os.getcwd())

        else :
            if isCommandExe(command):
                runCommandExe(rawInput)

            else:
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


def isCommandExe(command):
    return shutil.which(command) != None

def runCommandExe(rawCommand):
    subprocess.run(rawCommand , check=False)

if __name__ == "__main__":
    main()


# fix the panic mod , err handing
