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


file_name = "foods.txt"
file_variable = open(file_name, "r", encoding="utf-8")
foods = read_foods(file_variable)
for i in foods:
    print(i)
file_variable.close
