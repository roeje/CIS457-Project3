import cPickle as pickle
import sys
import os

# Class that contains save and load functionality
from cPickle import PickleError


class IO:
    def __init__ (self):
        return

    # Save an object to provided file
    def save_obj (self, obj, file_name, t):
        file = open(file_name, t)

        # Check for basic pickling error
        try:
            pickle.dump(obj, file)
        except PickleError as e:
            return False

        file.close()
        return True

    # Load object from specified file
    def load_obj (self, file_name):

        # File and pickle error checking
        try:
            file = open(file_name)
        except IOError as e:
            return False

        if os.fstat(file.fileno()).st_size == 0:
            return False
        else:
            try:
                new_obj = pickle.load(file)
            except PickleError as e:
                return False

        file.close()
        return new_obj