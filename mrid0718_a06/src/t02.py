"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports

# Constants


from Priority_Queue_linked import Priority_Queue


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


source = Priority_Queue()

source.insert("sanrio")
source.insert("kuromi")
source.insert("cinnamoroll")

print(source._front._value)
print(source._rear._value)
print(source.is_empty())
for v in source:
    print(v)
removed = source.remove()
print(f'Removed value: {removed}')
peeked = source.peek()
print(f'Peeked value: {peeked}')
source.insert("cinnamoroll")
target = Priority_Queue()
target.insert("hi")
target.insert("hello")
target.insert("bye")

target.combine(target, source)
for i in target:
    print(i)
