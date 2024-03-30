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


lst = List()
lst.append(2)
lst.append(4)
lst.append(6)
lst.append(6)
lst.append(8)

n = lst.count(6)
print(f'The number 6 appears {n} times in the list')

max_value = lst.max()
print(f'Maximum value: {max_value}')

min_value = lst.min()
print(f'Minimum value: {min_value}')
