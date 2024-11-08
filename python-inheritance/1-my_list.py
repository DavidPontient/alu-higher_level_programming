class MyList(list):
    """ A class that inherits from the built-in list class. """
    
    def print_sorted(self):
        """ Prints the list in ascending order. """
        print(sorted(self))
