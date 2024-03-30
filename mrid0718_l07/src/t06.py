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


lst = List()
lst.append(2)
lst.append(4)
lst.append(6)
print("List")
current = lst._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

lst.reverse_r()
print("Reversed")
current = lst._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()
