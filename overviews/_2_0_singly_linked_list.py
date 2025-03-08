### SINGLY LINKED LIST ###

# Linked lists are data structures consisting of Elements (nodes) connected via pointers, rather than stored contiguously in memory. 
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

    def __repr__(self):
        return f"SinglyLinkedList({self.to_array()})"

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

    def __len__(self):
        return self.length

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
        # Get the node just before the insertion point using the helper
        previous = self.get_node_at_position(position - 1)
        
        # Insert the new node by adjusting pointers
        new_node.next = previous.next
        previous.next = new_node
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

    def delete_node(self, node: Node):
        if not self.head:
            raise Exception("Linked list is empty. Nothing to delete.")
        
        # If the node to delete is the head node
        if node == self.head:
            self.head = self.head.next
            # If the list becomes empty after deletion, update tail
            if self.head is None:
                self.tail = None
            self.length -= 1
            return

        prev = None
        current = self.head

        # Traverse the list until the node is found
        while current is not None and current != node:
            prev = current
            current = current.next

        # If the node was not found in the list, raise an exception
        if current is None:
            raise Exception("Provided Node not in list. Nothing to delete.")

        # Delete the node by updating the previous node's next pointer
        prev.next = current.next
        # If the deleted node was the tail, update the tail pointer
        if current == self.tail:
            self.tail = prev

        self.length -= 1

    def delete_first_occurance(self, key):
        current = self.head
        while current:
            if current.data == key:
                self.delete_node(current)
                return  # Node deleted; exit the function
            current = current.next
        # Optionally, you could raise an exception here instead of printing.
        raise Exception("Node with key not found.")

    def delete_at_position(self, position: int):
        """Delete node at provided position in the list

        Args:
            position (int): Position of node (1 indexed) to be deleted
        """
        node_to_delete = self.get_node_at_position(position)
        self.delete_node(node_to_delete)

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

    def get_node_at_position(self, position: int):
        if position < 1 or position > self.length:
            raise Exception(f"Invalid position. Position: {position} | Allowed: 1 to {self.length}.")
        current = self.head
        for _ in range(1, position):
            current = current.next
        return current
    
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
        
    def sort(self):
        """Sort the linked list using merge sort."""
        if self.head is None or self.head.next is None:
            return  # Already sorted if empty or one element
        self.head = self._merge_sort(self.head)
        # Update tail pointer after sorting
        current = self.head
        while current.next:
            current = current.next
        self.tail = current

    def _merge_sort(self, head):
        """Recursively sort the list starting from head and return new head."""
        if head is None or head.next is None:
            return head
        
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # Split the list into two halves

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        """Find the middle node of the list starting from head."""
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        """Merge two sorted linked lists and return the head of the merged list."""
        if left is None:
            return right
        if right is None:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result
    
    def sorted_merge_iterative(self, left, right):
        # Create a dummy node to simplify edge cases
        dummy = self.Node(0)
        current = dummy

        # While both lists have nodes, compare and attach the smaller one.
        while left is not None and right is not None:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Attach the remaining nodes (only one of these will be non-None).
        if left is not None:
            current.next = left
        else:
            current.next = right

        # The merged list is in dummy.next.
        return dummy.next
    
    def remove_duplicates(self):
        if self.length == 0:
            raise Exception("Linked list is empty. Nothing to display.")
        elif self.length == 1:
            return self.head
        
        self.sort()
        current = self.head

        while current:
            next_node = current.next
            # Skip over duplicates
            while next_node and current.data == next_node.data:
                next_node = next_node.next
                self.length -= 1  # decrease length for each duplicate removed

            # If we've reached the end, update the tail pointer to the current node.
            if next_node is None:
                self.tail = current
            
            # Link the current node to the next distinct node.
            current.next = next_node
            current = next_node

        return


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

    sll.delete_first_occurance(3)
    print("\ndelete_first_occurance(3)")
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

    print(repr(sll))  # This calls sll.__repr__() behind the scenes.

