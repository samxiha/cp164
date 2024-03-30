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

from Food import Food
from Food_utilities import read_foods
from List_array import List
from copy import deepcopy


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
flist = List()
for food in foods:
    flist.append(food)

# eq
source = List()
source.append(foods[0])
target = List()
target.append(foods[0])
equals = source == target
print(f'The lists are equal: {equals}')

# getitem
value = flist[0]
print(f'Get item: {value}')

# clean
flist.clean()
print("Cleaned list: ", [str(food) for food in flist])

# combine
source1 = List()
source1.append(foods[0])
source2 = List()
source2.append(foods[1])
flist.combine(source1, source2)
print("Combined list:", [str(food) for food in flist])

# intersection
list1 = deepcopy(flist)
list2 = deepcopy(flist)
list1.intersection(list1, list2)
print("List after intersection:", [str(food) for food in flist])

# prepend
value = Food("Chicken", 1, False, 20)
flist.prepend(value)
print("Prepended list: ", [str(food) for food in flist])

# remove front
flist.remove_front()
print("List after removed value: ", [str(food) for food in flist])

# remove many
flist.remove_many(flist[0])
print("List after remove_many:", [str(food) for food in flist])

# split
list1, list2 = flist.split()
print("List 1 after split:", [str(food) for food in list1])
print("List 2 after split:", [str(food) for food in list2])

# split alt
list1, list2 = flist.split_alt()
print("List 1 after split_alt:", [str(food) for food in list1])
print("List 2 after split_alt:", [str(food) for food in list2])

# union
source1 = List()
source2 = List()
source1.append(foods[0])
source2.append(foods[1])
flist.union(list1, list2)
print("List after union:", [str(food) for food in flist])
