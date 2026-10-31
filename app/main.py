import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:

        sys.stdout.write("$ ")
        command = input()

        # get the first word
        parts = command.split()
        command = parts[0]
        args = parts[1:]
        # get rest words
        # print the words

        if command == "exit" :
            break
        elif command == "echo" :
            print(" ".join(args))
        else : 
            print(command + ": command not found")

        




    pass


if __name__ == "__main__":
    main()
