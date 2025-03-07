# Queues are abstract data types (ADT) defined by the FIFO principle: First-In-First-Out

# As queue are ADT's, they can be implemented in different ways, such as:
# Array-Based Implementation (Circular Queue):
# Using a dynamic or fixed-size array with circular buffering to efficiently manage the front and rear indices.
# Linked List-Based Implementation:
# Using a linked list where elements are enqueued at the tail and dequeued from the head, ensuring O(1) operations.
# Two-Stack Implementation:
# A queue can be implemented using two stacks, where one stack handles enqueuing and the other handles dequeuing.
# Specialized Libraries:
# Many programming languages offer built-in or optimized queue implementations (e.g., Python’s collections.deque, which provides efficient FIFO operations).

# Think Queues when:
# Elements must be processed in the order they arrive, keeping the order is important. Task Scheduling, job processing, buffering data streams.
# Breadth first travel - a queue is used to explore nodes by level
# Manage tasks or requests in systems (print ques, network packet buffers)
# Ensuring fairness

# Queue time complexities
# View item at front of queue O(1)
# peek()
# Dequeue item at front/top of queue O(1)
# dequeue()/popleft()
# Enqueue item at back/bottom of queue O(1)
# enqueue()/append()

# Initialise Empty "stack"

### QUEUES ###
# Python’s collections.deque is ideal for queues because it provides O(1) time complexity for both append and popleft operations.
# Do not use lists for ques, as the dequeue (popleft) action results in shifting of elements to the left

# Key Operations:
# Enqueue: Use append()
# Dequeue: Use popleft()

from collections import deque
queue_deque = deque()

queue_deque.append('a')
queue_deque.append('b')
queue_deque.append('c')

print("Queue after enqueues", queue_deque)
# dequeue is done using the pop left action
first_element = queue_deque.popleft()
print('Dequeued element', first_element)
print("Queue after Dequeue", queue_deque)