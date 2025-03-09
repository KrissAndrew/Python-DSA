from my_code.overviews._2_1_doubly_linked_list import DoublyLinkedList
from my_code._2_1_doubly_linked_list_problems.dll_dynamic_test_function import run_dll_tests

# Test sorting of a doubly linked list

if __name__ == "__main__":

    test_cases = [
        ([], Exception),             #  1
        ([1], [1]),                  #  2
        ([1, 2, 3], [3, 2, 1]),      #  3
        ([1, 2, 3, 4], [4, 3, 2, 1]) #  4
    ]

    dll = DoublyLinkedList()
    run_dll_tests(dll, dll.reverse_list(), test_cases)
