"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports

# Constants

from BST_linked import BST
from functions import do_comparisons, comparison_total
from Letter import Letter


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


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()
for value in DATA1:
    var = Letter(value)
    bst1.insert(var)

for value in DATA2:
    var = Letter(value)
    bst2.insert(var)

for value in DATA3:
    var = Letter(value)
    bst3.insert(var)

fn = "miserables.txt"
file = open(fn, "r", encoding="utf-8")
do_comparisons(file, bst1)
t1 = comparison_total(bst1)
file = open(fn, "r", encoding="utf-8")
do_comparisons(file, bst2)
t2 = comparison_total(bst2)
file = open(fn, "r", encoding="utf-8")
do_comparisons(file, bst3)
t3 = comparison_total(bst3)
print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("{}".format(t1))
print("------------------------------------------------------------")
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print("{}".format(t2))
print("------------------------------------------------------------")
print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print("{}".format(t3))
print("------------------------------------------------------------")
