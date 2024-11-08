#!/usr/bin/python3
''' Check if the object is an exact instance of the specified class '''


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of the class."""
    return type(obj) is a_class
