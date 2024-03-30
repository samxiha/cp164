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
from Food_utilities import calories_by_origin


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


food = Food("Naan", 2, True, 5)
food1 = Food("Butter chicken", 2, False, 67)
food2 = Food("Beef", 3, False, 12)
food3 = Food("Juice", 1, True, 0)
foods = [food, food1, food2, food3]
by_origin = calories_by_origin(foods, 2)
print(f'Calories: {by_origin}')
