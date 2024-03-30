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


source1 = Stack()
source2 = Stack()
l = [8, 12, 8, 5]
for v in l:
    source1.push(v)

l2 = [14, 9, 7, 1, 6, 3]
for x in l2:
    source2.push(x)

target = Stack()
target.combine(source1, source2)
for t in target:
    print(t)
