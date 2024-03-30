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
target1, target2 = source.split_alt()
print(target1._values)
print(target2._values)
