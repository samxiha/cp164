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


from Food_utilities import get_vegetarian, read_foods


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


file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)
v_foods = get_vegetarian(foods)
for i in v_foods:
    print(i)
    print()
file_variable.close
