"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports

# Constants

from Stack_array import Stack
from utilities import stack_to_array


stack = Stack()

stack.push(9)
stack.push(10)
stack.push(1)
stack.push(0)
stack.push(4)

target = []
stack_to_array(stack, target)
print("Array: ", target)
