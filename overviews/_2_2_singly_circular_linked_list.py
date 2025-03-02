### SINGLY CIRCULAR LINKED LIST ###

# Singly Circular Linked List: The last node points back to the first node, forming a circle.
# Important to note - circular linked lists can infinitly loop if not implemented correctly
# 

### Singly Circular Linked List Class Implementation ###

# Node: Each element in a linked list is a node that contains data and one or more pointers (or references) to the next node (and possibly the previous node).
class SinglyCircularLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        if not self.head:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

    def __reversed__(self):
        if not self.head:
            return
        # Collect nodes in a list to facilitate reverse iteration
        nodes = []
        current = self.head
        count = 0
        while True:
            nodes.append(current.data)
            current = current.next
            if current == self.head:
                break
        # Yield nodes in reverse order
        for data in reversed(nodes):
            yield data

    def insert_at_beginning(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_node(self, key):
        if self.length == 0:
            print("Linked list is empty. Nothing to delete.")
            return

        current = self.head
        prev = self.tail

        while True:
            if current.data == key:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                self.length -= 1
                return
            prev = current
            current = current.next
            if current == self.head:
                break

        print("Node with key not found.")

    def pop(self):
        if self.length == 0:
            print("Linked list is empty. Nothing to pop.")
            return None

        if self.length == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return data

        current = self.head
        prev = None

        while current.next != self.head:
            prev = current
            current = current.next

        data = current.data
        prev.next = self.head
        self.tail = prev
        self.length -= 1
        return data

    def display_list(self):
        if self.length == 0:
            print("Linked list is empty. Nothing to display.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

    def generate_list_from_array(self, array):
        for data in array:
            self.insert_at_end(data)

    def reverse_list(self):
        if self.length == 0:
            print("Linked list is empty. Nothing to reverse.")
            return

        prev = self.tail
        current = self.head

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break

        self.head, self.tail = self.tail, self.head
        self.tail.next = self.head

# Example usage:
if __name__ == "__main__":
    scll = SinglyCircularLinkedList()
    scll.generate_list_from_array([1, 2, 3, 4, 5])
    scll.display_list()

    print("\nForward iteration:")
    for data in scll:
        print(data, end=" ")
    print()

    print("\nReverse iteration:")
    for data in reversed(scll):
        print(data, end=" ")
    print()

    scll.delete_node(3)
    print("\nAfter deleting node with data 3:")
    scll.display_list()

    print("\nReversing the list:")
    scll.reverse_list()
    scll.display_list()

    print("\nInserting 6 at the beginning:")
    scll.insert_at_beginning(6)
    scll.display_list()

    print("\nInserting 7 at the end:")
    scll.insert_at_end(7)
    scll.display_list()

    print("\npop() -> " + str(scll.pop()))
    scll.display_list()
