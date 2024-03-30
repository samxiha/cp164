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


from functions import vowel_count


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
count = vowel_count(s)
print(f'Number of vowels in {s}: {count}')
