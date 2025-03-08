# Test in-place (without extra memory) reversal of a singly linked list
if __name__ == "__main__":

    from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
    from my_code._2_0_linked_list_problems.sll_dynamic_test_function import sll_run_tests

    test_cases = [
        ([], Exception),             #  1
        ([1], [1]),                  #  2
        ([1, 2, 3], [3, 2, 1]),      #  3
        ([1, 2, 3, 4], [4, 3, 2, 1]) #  4
    ]

    sll = SinglyLinkedList()
    print("Running tests for reverse_list()...")
    sll_run_tests(sll, sll.reverse_list, test_cases)