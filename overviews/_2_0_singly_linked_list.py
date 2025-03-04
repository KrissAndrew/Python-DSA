### SINGLY LINKED LIST ###

# Elements (nodes) are connected via pointers, rather than stored contiguously in memory. 
# Allows for dynamic memory usage and can efficiently handle insertions and deletions.
# Unlike arrays, linked lists can grow or shrink during execution, ideal when the maximum number of elements isn’t known in advance.

# Advantages
# Efficient Insertions/Deletions: Inserting or deleting a node (especially at the beginning or in the middle) can be done in constant time, O(1), if you have the appropriate pointer.
# No Memory Waste: Memory is allocated as needed; there’s no need for pre-allocation like in static arrays.

# Trade-Offs
# No Random Access: To access the n-th element, you must traverse the list from the head, resulting in O(n) time complexity.
# Extra Memory Overhead: Each node requires additional storage for pointers.

# Comparison to arrays
# Arrays have a disadvantage due to the possibility of "holes" when data is inserted or deleted.
# Linked lists swap out the advantage of O(1) index look up times for the benefit of O(1) insertion and deletions
# Finding an arbitrary item in either still takes O(n) - begin to look into alternatives when searching is a priority

# Linked List time complexities
# Search
# Arbitrary index O(n) - May have to search all items
# Insert
# Insert item at front/end O(1) - Simply shift and undate pointers
# Insert item at arbitrary position O(n)
# Delete
# Delete item at front/end O(1) - Simply shift and undate pointers
# Delete item at arbitrary position O(n)

### Singly Linked List Class Implementation ###

# Node: Each element in a linked list is a node that contains data and one or more pointers (or references) to the next node (and possibly the previous node).
class SinglyLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.length == 0:
            raise Exception("Linked list is empty. Nothing to display.")
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __reversed__(self):
        self.reverse_list()
        current = self.head
        while current:
            yield current
            current = current.next
        # Restore original order
        self.reverse_list()

    # O(1) - point the new node to the head or assign it if no head exists
    def insert_at_beginning(self, data): 
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        # For an empty list, new node becomes both head and tail.
        if self.length == 0:
            self.tail = new_node
        self.length += 1


    # O(1) - point the new node to the head or assign it if no head exists
    def insert_at_end(self, data):
        new_node = self.Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            # For an empty list, new node becomes both head and tail.
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def insert_at_position(self, data, position: int):
        # Allow insertion from 1 up to self.length + 1 (1-indexed)
        if position < 1 or position > self.length + 1:
            raise Exception(f"Invalid position. Position: {position} | Allowed: 1 to {self.length + 1}.")
        
        # Insertion at the beginning
        if position == 1:
            self.insert_at_beginning(data)
            return
        
        # Insertion at the end
        if position == self.length + 1:
            self.insert_at_end(data)
            return

        new_node = self.Node(data)
        current = self.head
        # Traverse to the node just before the insertion point
        for _ in range(1, position - 1):
            current = current.next

        # Insert the new node
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    # O(n) - needs to assign new node items for each item in provided array
    def generate_list_from_array(self, array: list[int]):
        self.length = 0
        self.head = None
        self.tail = None
        for data in array:
            self.insert_at_end(data)


    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


    # O(n) - the item may be at the end of the list
    def delete_node(self, key):
        if self.length == 0:
            raise Exception("Linked list is empty. Nothing to delete.")
        
        prev = None
        current = self.head
        
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                if current == self.tail:
                    self.tail = prev
        
                self.length -= 1
                return # Stop once done, no need to keep processing

            prev = current
            current = current.next

        print("Node with key not found.")


    # O(n) - disadvantage of singly linked lists, popping must traverse entire data structure
    def pop(self):
        if self.length == 0:
            raise Exception("Linked list is empty. Nothing to pop.")
        
        elif self.length == 1:
            data = self.tail.data
            self.head = None
            self.tail = None
            self.length -= 1
            print("Linked list is now empty.")
            return data
        
        else:
            prev = self.head
            current = self.head.next

            while current.next:
                prev = current
                current = current.next

            prev.next = None
            self.tail = prev
            self.length -= 1
            return current.data
    

    # O(n) - must traverse entire array
    def reverse_list(self):
        if self.length == 0:
            raise Exception("Linked list is empty. Nothing to reverse.")
        else:
            prev = None
            current = self.head
            self.head = self.tail # Swap head and tail
            self.tail = current
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

    # Getters

    # Can get directly but should be avoided
    def get_head_node(self):
        if self.head: return self.head

    def get_tail_node(self):
        if self.tail: return self.tail
    
    # O(N) linear running time complexity
    def get_middle_node(self):
        if self.length == 0:
            raise Exception("Linked list is empty. Nothing to display.")
        elif self.length == 1:
            return self.head
        
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next and fast_pointer.next.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return slow_pointer
    
    # Setters

    def set_head_data(self, data):
        if self.head:
            self.head.data = data
        else:
            raise Exception("Linked list is empty. Cannot set head data.")

    def set_tail_data(self, data):
        if self.tail:
            self.tail.data = data
        else:
            raise Exception("Linked list is empty. Cannot set tail data.")
    

if __name__ == "__main__":
    # Initilize single linked list
    sll = SinglyLinkedList()
    arr = [1,2,3,4,5]
    print("generate_list_from_array")
    sll.generate_list_from_array(arr)
    print(sll)

    # Forward iteration using __iter__
    print("Forward iteration:")
    for data in sll:
        print(data, end=" ")
    print()

    # Reverse iteration using __reversed__
    print("Reverse iteration:")
    for data in reversed(sll):
        print(data, end=" ")
    print()

    sll.delete_node(3)
    print("\ndelete_node(3)")
    print(sll)

    print("\nreverse_list()")
    sll.reverse_list()
    print(sll)

    print("\ninsert_at_beginning(3)")
    sll.insert_at_beginning(3)
    print(sll)

    print("\ninsert_at_end(1)")
    sll.insert_at_end(1)
    print(sll)

    print("\npop() -> " + str(sll.pop()))
    print(sll)

    print("\nget_middle_node()")
    print(sll.get_middle_node().data)
    print(sll)

    print("\nto_array()")
    print(sll.to_array())
