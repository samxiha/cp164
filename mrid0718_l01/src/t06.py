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


from Food_utilities import read_foods, write_foods


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


file_name = "foods.txt"
file_variable = open(file_name, "r", encoding="utf-8")
foods = read_foods(file_variable)
file_variable.close

file_name = "new_foods.txt"
file_variable = open(file_name, "w", encoding="utf-8")
write_foods(file_variable, foods)
file_variable.close
