"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports

# Constants

from utilities import stack_test
from Food import Food


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


l = Food("Lasagna", 7, False, 135)
b = Food("Butter Chicken", 2, False, 490)
foods = [l, b]
stack_test(foods)
