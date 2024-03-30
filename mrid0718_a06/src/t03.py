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


from Deque_linked import Deque


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


source = Deque()
source.insert_front("cinnamoroll")
source.insert_rear("kuromi")
for v in source:
    print(v)
empty = source.is_empty()
print(f'Empty: {empty}')
print('Removed from front:', source.remove_front())
print('Removed from rear:', source.remove_rear())
empty = source.is_empty()
print(f'Empty: {empty}')
