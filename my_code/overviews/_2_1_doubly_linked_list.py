# Elements (nodes) are connected via pointers, rather than stored contiguously in memory. 
# Allows for dynamic memory usage and can efficiently handle insertions and deletions.
# Unlike arrays, linked lists can grow or shrink during execution, ideal when the maximum number of elements isn’t known in advance.

# Advantages
# Efficient Insertions/Deletions: Inserting or deleting a node (especially at the beginning or in the middle) can be done in constant time, O(1), if you have the appropriate pointer.
# No Memory Waste: Memory is allocated as needed; there’s no need for pre-allocation like in static arrays.

# Trade-Offs
# No Random Access: To access the n-th element, you must traverse the list from the head, resulting in O(n) time complexity.
# Extra Memory Overhead: Each node requires additional storage for pointers.

### DOUBLY LINKED LISTS ###

# Preferred over singly linked list when flexibility in navigating and manipulating the list is needed. Key scenarios include:

# Bidirectional Traversal: If your application requires moving both forward and backward through the list
# (e.g., undo/redo feature or browser back/forward history), the extra pointer to the previous node makes backward traversal straightforward.

# Efficient Deletion or Insertion: When you need to remove or insert nodes frequently, especially in the middle of the list.
# Having a pointer to the previous node lets you perform these operations in O(1) time. 
#! Note - This is only true when the node to be deleted is known - which is often not the case
# In a singly linked list, you often have to traverse from the head to find the previous node, which adds overhead.


### Doubly Linked List Class Implementation ###

class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None # Fundamental difference in DLL - node awareness of prev node
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.data
            current = current.prev

    def __str__(self):
        if self.length == 0:
            return "Empty list"  # Instead of raising an exception
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return "None → " + " ↔ ".join(values) + " → None"

    # O(1) - simple, only change needed it updating head.prev to new
    def insert_at_beginning(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            # For an empty list, new node becomes both head and tail.
            self.head = new_node
            self.tail = new_node
        self.length += 1


    def delete_node(self, key):
        if self.length == 0:
            print("Linked list is empty. Nothing to delete.")
            return

        current = self.head

        while current:
            if current.data == key:
                # If current is the head node
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        # List is now empty
                        self.tail = None

                # If current is the tail node
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None

                # If current is an intermediate node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.length -= 1
                return  # Node found and deleted; exit the function

            current = current.next

        print("Node with key not found.")

    # O(1) - Advantage of singly linked lists, popping does not need to traverse entire data structure
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
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return self.tail.data

    # Utility function to find the middle of a linked list (for merge sort)
    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Merge two sorted sublists
    def merge_sorted_lists(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge_sorted_lists(left.next, right)
            if result.next:
                result.next.prev = result
        else:
            result = right
            result.next = self.merge_sorted_lists(left, right.next)
            if result.next:
                result.next.prev = result

        return result

    # Merge Sort Algorithm for DLL
    def merge_sort(self, head):
        if not head or not head.next:
            return head  # Base case: 0 or 1 element in list

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # Split the list into two halves

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        return self.merge_sorted_lists(left, right)

    # Sort the doubly linked list
    def sort_list(self):
        if not self.head or not self.head.next:
            return  # List is already sorted (0 or 1 element)

        self.head = self.merge_sort(self.head)

        # Reset the tail pointer after sorting
        current = self.head
        while current.next:
            current = current.next
        self.tail = current
        self.sorted = True


    def sorted_insert(self, data):
        """ Inserts a node in a sorted manner into a doubly linked list. """
        new_node = self.Node(data)

        # Case 1: If the list is empty, set the head and tail
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Case 2: Insert at the beginning if it's smaller than the head node
        if data <= self.head.data:  # Allow duplicates at the start
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head

        # Traverse to find the correct insertion point
        while current.next and current.data <= data:  # Allow insertion after duplicates
            current = current.next

        # Case 3: Insert at the end
        if not current.next and current.data <= data:
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
            return

        # Case 4: Insert in the middle
        prev_node = current.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = current
        current.prev = new_node



    def display_list(self):
        if not self.head:
            print("Linked list is empty.")
            return
        print("None", end=" → ")

        current = self.head
        while current:
            if current.next:  # If there's another node ahead, use ↔
                print(current.data, end=" ↔ ")
            else:  # Last node, use → None
                print(current.data, end=" → None")
            current = current.next

        print()  # Newline for better formatting

    
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

    def reverse_list(self):
        if self.length == 0:
            Exception("Linked list is empty. Nothing to reverse.")
        else:
            current = self.head
            while current:
                # Swap the next and prev pointers
                current.prev, current.next = current.next, current.prev
                # Move to the next node in the original sequence
                current = current.prev

        # Swap the head and tail pointers
        self.head, self.tail = self.tail, self.head

if __name__ == "__main__":
    # Initilize single linked list
    dll = DoublyLinkedList()
    arr = [1,2,3,4,5]
    print("generate_list_from_array")
    dll.generate_list_from_array(arr)
    print(dll)
    
    # Forward iteration using __iter__
    print("Forward iteration:")
    for data in dll:
        print(data, end=" ")
    print()

    # Reverse iteration using __reversed__
    print("Reverse iteration:")
    for data in reversed(dll):
        print(data, end=" ")
    print()
    
    dll.delete_node(3)
    print("\ndelete_node(3)")
    print(dll)
    
    print("\nreverse_list()")
    dll.reverse_list()
    print(dll)

    print("\ninsert_at_beginning(3)")
    dll.insert_at_beginning(3)
    print(dll)
    
    print("\ninsert_at_end(1)")
    dll.insert_at_end(1)
    print(dll)

    print("\npop() -> " + str(dll.pop()))
    print(dll)

    arr = [4, 2, 5, 1, 3]
    
    print("Inserting elements:")
    for num in arr:
        dll.insert_at_end(num)
    
    print(dll)

    print("\nSorting list...")
    dll.sort_list()
    print(dll)

    dll.sorted_insert(1)
    print(dll)


