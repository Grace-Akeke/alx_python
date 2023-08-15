#!/usr/bin/python3
import sys

def main():
    # get the number of  arguments
    num_args = len(sys.argv) - 1
    #print number of arguements and their values
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
#to inexecute the imported module
if __name__ == "__main__":
    main()