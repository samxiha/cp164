"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports

# Constants

from List_linked import List


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


list1 = List()
list2 = List()
list1.append(1)
list1.append(2)
list1.append(3)

list2.append(3)
list2.append(2)
list2.append(1)

target = List()

target.union_r(list1, list2)
print(target._front._value, target._front._next._value,
      target._front._next._next._value)
