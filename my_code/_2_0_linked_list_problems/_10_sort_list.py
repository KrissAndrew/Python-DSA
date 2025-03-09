from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import run_sll_tests

# Test sorting of a singly linked list 
if __name__ == "__main__":

    test_cases = [
        ([], []),                           #  1
        ([1], [1]),                         #  2
        ([2, 1], [1, 2]),                   #  3
        ([1, 3, 2], [1, 2, 3]),             #  4
        ([3, 2, 1, 0, -1], [-1, 0, 1, 2, 3]),  #  4
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), #  4
    ]

    sll = SinglyLinkedList()
    run_sll_tests(sll, sll.sort, test_cases)