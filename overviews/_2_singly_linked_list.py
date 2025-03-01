### SINGLY LINKED LISTS ###

# Linked lists are data structures where elements (nodes) are connected via pointers, rather than stored contiguously in memory. 
# This structure offers dynamic memory usage and can efficiently handle insertions and deletions.
# Unlike arrays, linked lists can grow or shrink during execution, making them ideal when the maximum number of elements isn’t known in advance.

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

    # O(1) - Simply point the new node to the head or assign it if no head exists
    def insert_at_beginning(self, data): 
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        # For an empty list, new node becomes both head and tail.
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    # O(1) - Simply point the new node to the head or assign it if no head exists
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
    
    # O(n) - the item may be at the end of the list
    def delete_node(self, key):
        if self.length == 0:
            print("Linked list is empty. Nothing to delete.")
            return
        
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
            print("Linked list is empty. Nothing to pop.")
            return None
        
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

            data = current.data
            prev.next = None
            self.tail = prev
            self.length -= 1
            return data
    
    # O(n) - iterate over all items
    def display_list(self):
        if self.length == 0:
            print("Linked list is empty. Nothing to display.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
    
    # O(n) - needs to assign new node items for each item in provided array
    def generate_list_from_array(self, array):
        for data in array:
            self.insert_at_end(data)

    # O(n) - must traverse entire array
    def reverse_list(self):
        if self.length == 0:
            print("Linked list is empty. Nothing to reverse.")
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

if __name__ == "__main__":
    # Initilize single linked list
    SLL = SinglyLinkedList()
    arr = [1,2,3,4,5]
    print("generate_list_from_array")
    SLL.generate_list_from_array(arr)
    SLL.display_list()
    SLL.delete_node(3)
    
    print("\ndelete_node(3)")
    SLL.display_list()
    
    print("\nreverse_list()")
    SLL.reverse_list()
    SLL.display_list()

    print("\ninsert_at_beginning(3)")
    SLL.insert_at_beginning(3)
    SLL.display_list()
    
    print("\ninsert_at_end(1)")
    SLL.insert_at_end(1)
    SLL.display_list()

    print("\npop() -> " + str(SLL.pop()))
    SLL.display_list()
