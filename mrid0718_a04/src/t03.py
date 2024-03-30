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

from Queue_array import Queue
from functions import queue_split_alt


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


source = Queue()
source.insert(2)
source.insert(4)
source.insert(6)
source.insert(8)
print(source._values)
target1, target2 = queue_split_alt(source)
print(target1._values, target2._values)
