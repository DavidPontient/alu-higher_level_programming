#!/usr/bin/python3
'''A function that returns the available atts and methods of an object '''


def lookup(obj):
    """Returns a list of available attributes and methods of the object."""
    return dir(obj)
