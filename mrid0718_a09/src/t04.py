"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports

# Constants


from BST_linked import BST


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


bst = BST()

bst.insert(1)
bst.insert(21)
bst.insert(321)
bst.insert(4321)
bst.insert(54321)
bst.insert(6542321)

zero, one, two = bst.node_counts()

print(zero)
print(one)
print(two)

print(210 in bst)

val = bst.parent(20)

val2 = bst.parent_r(20)

print(val, val2)
