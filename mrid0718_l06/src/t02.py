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


l = List()
l.append(2)
l.append(4)
l.append(6)
l.append(8)
l.append(10)

previous, current, index = l._linear_search(6)

print("Previous value:", previous._value if previous else None)
print("Current value:", current._value if current else None)
print("Index:", index)
