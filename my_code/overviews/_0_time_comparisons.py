import time
from _2_0_singly_linked_list import SinglyLinkedList
from _2_1_doubly_linked_list import DoublyLinkedList
from _2_2_singly_circular_linked_list import SinglyCircularLinkedList

if __name__ == "__main__":
    sll = SinglyLinkedList()
    dll = DoublyLinkedList()
    scll = SinglyCircularLinkedList()
    array = []

    now = time.time()    
    for i in range(500000):
        sll.insert_at_beginning(i)    
    print('Inserting items into singly linked list took %ss' % time.time() - now)

    now = time.time()    
    for i in range(500000):
        dll.insert_at_beginning(i)
    print('Inserting items into doubly linked list took %ss' % time.time() - now)

    now = time.time()    
    for i in range(500000):
        scll.insert_at_beginning(i)
    print('Inserting items into singly circular linked list took %ss' % time.time() - now)

    now = time.time()
    for i in range(500000):
        array.insert(0, i)
    print('Inserting items into singly circular linked list took %ss' % time.time() - now)