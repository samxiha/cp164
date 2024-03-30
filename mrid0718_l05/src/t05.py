"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import is_palindrome


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


s = input("Enter a string: ")
palindrome = is_palindrome(s)
print(f'Is a palindrome: {palindrome}')
