#!/usr/bin/python3
from add_0 import add

def main():
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format (a, b, result))
    #check if the script is running directly
    if __name__ == "__main__":
        main()