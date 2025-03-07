# Stacks are abstract data types (ADT) defined by the LIFO principle: Last-In-First-Out

# As stacks are ADT's, they can be implemented in different ways, such as:
# Array-Based Implementation:
# Using a dynamic array (e.g., Python’s list) where elements are added and removed from the end.
# Linked List-Based Implementation:
# Using a linked list where the head of the list represents the top of the stack, allowing O(1) push and pop operations.
# Fixed-Size Array:
# In lower-level languages, a stack might be implemented using a fixed-size array with manual management of the top index.
# Specialized Libraries:
# Some languages or libraries provide built-in or optimized stack implementations (e.g., using collections.deque in Python, which can be used as a stack).

# Think Stacks when:
# You need to “undo” actions or backtrack (for example, in parsing nested structures or implementing an undo feature)
# When a problem has a recursive nature, you can use a stack to emulate the call stack
# If the most recent item needs to be processed first, recording recent states or commands

# Stack time complexities
# View item on stop of stack O(1)
# peek()
# Append item to front/top of stack O(1)
# append/push()
# Delete item at front/top of stack O(1)
# pop()


# Python lists are a natural choice for stacks because they offer built-in methods for appending and popping elements efficiently at the end of the list.
# Initialise Empty "stack"
stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print("Stack after pushes", stack)

top_element = stack.pop()
print("Popped element:", top_element)
print("Stack after pop", stack)

# A double ended que can work just as well as a list for stack emulation
from collections import deque

de_que = deque()
de_que.append(('a', ord('a')))
de_que.append(('b', ord('b')))

print(de_que)
pop_char, pop_uni = de_que.pop()
print(f"[Char|Unicode] popped [{pop_char}|{pop_uni}]")



