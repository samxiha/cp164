"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-31"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list, list_to_array
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


llist = List()
source = [2, 4, 6, 8, 10]
array_to_list(llist, source)
print(llist._values, source)

target = []
list_to_array(llist, target)
print(llist._values, target)
