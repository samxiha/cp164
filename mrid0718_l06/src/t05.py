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
lst.append("kuromi")
lst.append("sanrio")
lst.append("cinnamoroll")
lst.append("pompompurin")

peek_value = lst.peek()
print(f'Peeked valuee: {peek_value}')

remove_value = lst.remove("pompompurin")
print(f'Removed value: {remove_value}')
