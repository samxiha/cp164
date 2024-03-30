"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
# Imports

# Constants


from Food_utilities import read_foods
from utilities import queue_test


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


fv = open("foods.txt", "r")
foods = read_foods(fv)
queue_test(foods)
