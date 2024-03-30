"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import stack_maze


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


maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['X', 'F'], 'F': ['G'], 'G': ['C']}
path = stack_maze(maze)
print("Path: ", path)
