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
lst.append("blue")
lst.append("yellow")
lst.append("red")

find_value = lst.find("blue")
print(f'Found: {find_value}')

index_value = lst.index("yellow")
print(f'Index of yellow: {index_value}')

contains_value = "red" in lst
print(f'Red is in the list: {contains_value}')
