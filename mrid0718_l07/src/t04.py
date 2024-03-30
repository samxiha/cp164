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


source1 = List()
source2 = List()
target = List()

source1.append(1)
source1.append(2)
source1.append(3)
source1.append(4)

source2.append(2)
source2.append(4)
source2.append(6)

target.intersection(source1, source2)
print(target._front._value, target._front._next._value)
