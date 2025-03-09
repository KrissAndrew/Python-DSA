from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import run_sll_tests

# Test removal of duplicated from a singly linked list

if __name__ == "__main__":

    test_cases = [
        ([], Exception),                           #  1
        ([1], [1]),                                #  2
        ([1, 1], [1]),                             #  3
        ([1, 2, 2, 3], [1, 2, 3]),                 #  4
        ([1, 1, 2, 2, 3, 3, 4, 4], [1, 2, 3, 4]),  #  5
        ([5, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),     #  6
    ]

    sll = SinglyLinkedList()
    run_sll_tests(sll, sll.remove_duplicates, test_cases)