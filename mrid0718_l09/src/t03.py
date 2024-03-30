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
from Hash_Set_array import Hash_Set
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


h = Hash_Set(5)
fn = "foods.txt"
file = open(fn, "r", encoding="utf-8")
foods = read_foods(file)
for f in foods:
    h.insert(f)

h.debug()
