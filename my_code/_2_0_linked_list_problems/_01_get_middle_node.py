import os
import sys
from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import sll_run_tests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Test in-place (without extra memory) return of middle node of a linked list
if __name__ == "__main__":

    test_cases = [
        ([], Exception),  #  1
        ([1], 1),         #  2
        ([1, 2, 3], 2),   #  3
        ([1, 2, 3, 4], 2) #  4
    ]

    def middle_extractor(sll, _):
        return sll.get_middle_node().data if sll.get_middle_node() else None

    sll = SinglyLinkedList()
    sll_run_tests(sll, sll.get_middle_node, test_cases, middle_extractor)