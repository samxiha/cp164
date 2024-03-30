"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
# Imports

# Constants


from utilities import array_to_pq
from Priority_Queue_array import Priority_Queue


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


source = [0, 1, 2, 3, 4, 5]
target = []
pq = Priority_Queue()
array_to_pq(pq, source)
for v in pq:
    print(v)
