from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import run_sll_tests

# Test insertion of an item at the start of a singly linked list 

def compare_linked_lists_extractor(inputs):
    """Compares two linked lists and returns True if they are identical."""
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for linked list comparison: {inputs}")
    
    list1, list2 = inputs  # Unpack (list1, list2)

    sll1, sll2 = SinglyLinkedList(), SinglyLinkedList()  # Create two linked lists
    sll1.generate_list_from_array(list1)
    sll2.generate_list_from_array(list2)

    return sll1.to_array() == sll2.to_array()  # Compare the lists

if __name__ == "__main__":
    
    test_cases = [
        (([], []), True),          # 1: Both lists empty → equal
        (([1], [1]), True),        # 2: Both lists contain 1 → equal
        (([1, 2], [2, 1]), False), # 3: Order matters → not equal
        (([1, 2, 3], []), False),  # 4: One list is empty → not equal
    ]

    run_sll_tests(None, None, test_cases, compare_linked_lists_extractor)  # No need for sll
