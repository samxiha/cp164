"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-02-14"
-------------------------------------------------------
"""
# Imports

# Constants


from Queue_linked import Queue


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

empty = source.is_empty()
print(empty)
print(source._front._value)
print(source._rear._value)
