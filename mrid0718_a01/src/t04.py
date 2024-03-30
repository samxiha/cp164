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


from functions import file_analyze


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


file_name = "customers.txt"
fv = open(file_name, 'r')
upp, low, dig, whi, rem = file_analyze(fv)
print(f'Uppercase: {upp}')
print(f'Lowercase: {low}')
print(f'Digits: {dig}')
print(f'Whitespace: {whi}')
print(f'Remaining: {rem}')
