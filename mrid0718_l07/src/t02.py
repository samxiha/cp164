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


source = List()
lst = List()
source.append("chips")
source.append("candy")
source.append("chocolate")
lst.append("kuromi")
lst.append("cinnamoroll")
lst.append("sanrio")

b = source.is_identical_r(lst)
print(f'The lists are identical: {b}')
