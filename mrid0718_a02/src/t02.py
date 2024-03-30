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
from Food_utilities import average_calories


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


f = Food("Lasagna", 7, False, 223)
f1 = Food("Butter Chicken", 2, False, 346)
f2 = Food("Moo Goo Guy Pan", 1, False, 381)
foods = [f, f1, f2]
avg = average_calories(foods)
print(f'average calories: {avg}')
