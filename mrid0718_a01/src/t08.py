"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import matrix_stats


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


a = [[5, 0, -7, 1], [4, 3, 5, 0], [6, -3, -6, 0]]
small, large, total, average = matrix_stats(a)
print(f'({small}, {large}, {total}, {average})')
