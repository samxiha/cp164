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
lst.append("pompompurin")
lst.append("sanrio")
lst.append("cinnamoroll")
lst.append("kuromi")

value = lst[1]
print(f"Value at index 1: {value}")

lst[1] = "kuromi"
print('Current value at index 1: ', lst[1])
