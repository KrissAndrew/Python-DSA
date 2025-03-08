# Construct an in-place (without extra memory) algorithm to find and return the middle node of a linked list
# Must be O(N) (linear) running time
# Examples: [1, 2, 3, 4] --> middle node is: 2,   [1, 2, 3, 4, 5] --> middle node is: 3

# For the sake of this I will implement a find_middle_node() function in my linked list classes
if __name__ == "__main__":

    from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
    from my_code._2_0_linked_list_problems.sll_dynamic_test_function import sll_run_tests

    test_cases = [
        ([], Exception),  #  1
        ([1], 1),         #  2
        ([1, 2, 3], 2),   #  3
        ([1, 2, 3, 4], 2) #  4
    ]

    def middle_extractor(sll, _):
        return sll.get_middle_node().data if sll.get_middle_node() else None

    sll = SinglyLinkedList()
    print("Running tests for get_middle_node()...")
    sll_run_tests(sll, sll.get_middle_node, test_cases, middle_extractor)