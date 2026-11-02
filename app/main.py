import sys


commnads = [
    "exit",
    "echo",
    "type",
]

def main():
    # TODO: Uncomment the code below to pass the first stage

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






    pass

def runType(command):

    if command in commnads :
        print(command + " is a shell builtin")
    else :
        print(command + ": not found")



if __name__ == "__main__":
    main()
