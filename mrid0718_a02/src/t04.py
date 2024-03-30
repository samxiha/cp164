"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports

# Constants

from Food import Food
from Food_utilities import food_table


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


f = Food("Lasagna", 7, False, 135)
f1 = Food("Butter Chicken", 2, False, 490)
f2 = Food("Moo Goo Guy Pan", 1, False, 272)
foods = [f, f1, f2]
food_table(foods)
