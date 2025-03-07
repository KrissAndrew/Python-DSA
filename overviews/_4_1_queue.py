class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __len__(self):
        return self.length

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            # Queue is empty, new node becomes head
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.head is None:
            raise Exception("Queue is empty.")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            # Queue is now empty, update tail too
            self.tail = None
        self.length -= 1
        return data

    def peek(self):
        if self.head is None:
            raise Exception("Queue is empty.")
        return self.head.data
    
    # O(n) - needs to assign new node items for each item in provided array
    def generate_queue_from_array(self, array: list[int]):
        self.length = 0
        self.head = None
        self.tail = None
        for data in array:
            self.insert_at_end(data)
    

if __name__ == "__main__":
    que_ints = [1, 2, 3, 4, 5]
    queue = Queue()
    queue.generate_queue_from_array(que_ints)
    print(queue.peek()) # 1
    