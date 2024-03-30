"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports

# Constants


from List_linked import List

from Sorted_List_linked import Sorted_List
from Food import Food


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


l = List()
l2 = List()
f1 = Food("Lasagna", 7, False, 135)
f2 = Food("Butter Chicken", 2, False, 490)
f3 = ("Moo Goo Guy Pan", 1, False, 272)
l.append(f1)
l.append(f2)
l.append(f3)
l2.append("sanrio")
l2.append("kuromi")
l2.append("cinnamoroll")
target = List()
target.combine(l, l2)
for v in target:
    print(v)

removed = target.remove_front()
print(f'Removed value: {removed}')
target1 = List()
target2 = List()
target1, target2 = target.split()
print("Target 1")
for i in target1:
    print(i)
print("Target2")
for j in target2:
    print(j)

sl = Sorted_List()
sl.insert("sanrio")
sl.insert("kuromi")
sl.insert("cinnamoroll")
value = sl.find("kuromi")
print(f'Found: {value}')
maxi = sl.max()
mini = sl.min()
print(f'Max: {maxi}')
print(f'Min: {mini}')
peeked = sl.peek()
print(f"Peeked: {peeked}")
n = sl.index("sanrio")
print(f'Index of "sanrio": {n}')
sl.insert("kuromi")
print("Original list:")
for v in sl:
    print(v)
cleaned = sl.clean()
print("Cleaned list:")
for v in sl:
    print(v)
sl2 = Sorted_List()
sl2.insert("pompompurin")
sl2.insert("sanrio")
sl2.insert("cinnamoroll")
target = Sorted_List()
print("Intersection: ")
target.intersection(sl, sl2)
for v in target:
    print(v)
