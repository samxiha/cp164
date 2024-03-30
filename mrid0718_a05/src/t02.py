"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports

# Constants

from Food_utilities import read_foods
from Sorted_List_array import Sorted_List


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


file = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file)

sl = Sorted_List()

for food in foods:
    sl.insert(food)

# __contains__
print(foods[0] in sl)

# __getitem__
value = sl[1]
print(value)

# clean
sl.clean()

# count
print(sl.count(foods[0]))

# find
print(sl.find(foods[0]))

# index
print(sl.index(foods[0]))

# intersection
sl2 = Sorted_List()
sl2.insert(foods[1])
sl2.intersection(sl, sl2)

# max
value = sl.max()
print(value)

# min
value = sl.min()
print(value)

# peek
value = sl.peek()
print(value)

# remove
value = sl.remove(foods[0])
print("Removed: ", value)

# remove_front
value = sl.remove_front()
print("Removed from front", value)

# remove_many
sl.remove_many(foods[1])

# split
target1, target2 = sl.split()

# split_alt
target1_alt, target2_alt = sl.split_alt()

# split_key
target1_key, target2_key = sl.split_key(foods[2])

# union
print(sl == sl)
