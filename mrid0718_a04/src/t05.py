"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports

# Constants

from Priority_Queue_array import Priority_Queue
from functions import pq_split_key


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


source = Priority_Queue()
source.insert(2)
source.insert(4)
source.insert(6)
source.insert(8)

key = 2
print(source._values)
target1, target2 = pq_split_key(source, key)
print(target1._values, target2._values)
