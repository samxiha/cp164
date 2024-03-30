"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants


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


source_stack = Stack()
for value in [1, 2, 3, 4, 5]:
    source_stack._values.append(value)

print("Original Stack:", source_stack._values)

source_stack.reverse()

print("Reversed Stack:", source_stack._values)
