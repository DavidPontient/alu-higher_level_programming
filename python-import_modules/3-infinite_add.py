#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    print(sum(int(arg) for arg in argv[1:]))
