#!/usr/bin/python3
"Creating a square "


class Square:
    '''
    Create a square
        Has a private Instance att: size
    '''

    def __init__(self, size):
        " initializing the pricate instance size"
        self.__size = size
