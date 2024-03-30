"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID:      169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports

# Constants


from Queue_circular import Queue


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


q = Queue()
empty = q.is_empty()
print(f'The queue is empty: {empty}')
for i in range(3):
    q.insert(i)
    print(f'Inserted {i}')
print("Peek: ", q.peek())
empty = q.is_empty()
print(f'The queue is empty: {empty}')
full = q.is_full()
print(f'The queue is full: {full}')
n = len(q)
print(f'The length of the queue is: {n}')
removed = q.remove()
print(f"Removed value: {removed}")

source = Queue()
for i in range(3):
    source.insert(i)
    print(f'Inserted {i}')

equals = q == source
if not equals:
    print("The queues are not equal")
else:
    print("The queues are equal")
