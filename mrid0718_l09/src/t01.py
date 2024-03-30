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

from functions import hash_table
from Food_utilities import read_foods


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


fn = "foods.txt"
file = open(fn, "r", encoding="utf-8")
foods = read_foods(file)
hash_table(7, foods)
file.close()
