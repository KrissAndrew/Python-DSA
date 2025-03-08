from _4_1_queue import Queue

# A double ended queue (deque) contains all functionality of a queue.
# The only addition is the ability to add items to the front of the queue.
# This is a good example of inheritance, the deque can inherit all pre-existing functionality of the queue

class DeQueue(Queue):
    def append_left(self, data):
        # Create a new node using the inner Node class from the parent Queue
        new_node = self.Node(data)
        # Insert the new node at the beginning of the queue
        new_node.next = self.head
        self.head = new_node
        
        # If the queue was empty, update the tail to point to the new node
        if self.length == 0:
            self.tail = new_node
        
        # Increase the length of the queue
        self.length += 1

if __name__ == "__main__":
    deque_ints = [1, 2, 3, 4, 5]
    deque_strings = ["string1", "string2", "string3", "string4", "string5"]
    deque_mixed = [True, 2, "string3", 4, True]

    int_queue = DeQueue()
    string_queue = DeQueue()
    mixed_queue = DeQueue()

    # Generate the queue from an array (inherited method)
    int_queue.generate_queue_from_array(deque_ints)
    print("Peek:", int_queue.peek())  # Should print 1
    
    # Append to the left of the queue
    int_queue.append_left(0)
    print("Peek after append_left:", int_queue.peek())  # Now should print 2

    # Dequeue to see the modified behavior if any override is applied
    print("Dequeue:", int_queue.dequeue())

        # Generate the queue from an array (inherited method)
    string_queue.generate_queue_from_array(deque_strings)
    print("Peek:", string_queue.peek())  # Should print 1
    
    # Append to the left of the queue
    string_queue.append_left("string0")
    print("Peek after append_left:", string_queue.peek())  # Now should print 2

    # Dequeue to see the modified behavior if any override is applied
    print("Dequeue:", string_queue.dequeue())

        # Generate the queue from an array (inherited method)
    mixed_queue.generate_queue_from_array(deque_mixed)
    print("Peek:", mixed_queue.peek())  # Should print 1
    
    # Append to the left of the queue
    mixed_queue.append_left(123)
    print("Peek after append_left:", mixed_queue.peek())  # Now should print 123

    # Dequeue to see the modified behavior if any override is applied
    print("Dequeue:", mixed_queue.dequeue())





