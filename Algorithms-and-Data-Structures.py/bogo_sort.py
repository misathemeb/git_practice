import random
# The sys.argv list gives us the command line arguments to the
# script. To use it, we also need to import the "sys" module.
import sys
# Here's where we import the load_numbers function from above.
from load import load_numbers

# pass the first command line argument (which should be
# the path to a file) to load_numbers, and store the returned list of
# numbers in a variable.
numbers = load_numbers(sys.argv[1]);

# print(numbers)

def is_sorted(values):
    for index in range (len(values) - 1):
        if values[index] > values[index + 1]:
            return False  
    return True

def bogo_sort(values):
    pass      