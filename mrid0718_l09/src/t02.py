"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports

# Constants


from Hash_Set_array import Hash_Set


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


h = Hash_Set(5)
lst = [1, 2, 3, 3]
for l in lst:
    h.insert(l)

for v in h:
    print(v)

removed = h.remove(3)
print("New list")
for v in h:
    print(v)
