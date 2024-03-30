"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports

# Constants

from Stack_array import Stack
from utilities import array_to_stack


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


s = Stack()
source = [6, 5, 4, 3, 2, 1]
array_to_stack(s, source)
for v in s:
    print(v)
