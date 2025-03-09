from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import run_sll_tests

# Test merging of two sorted singly linked lists.

def merge_extractor(_, inputs):
    """Extracts the merged sorted list from two given sorted lists."""
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for sorted_merge: {inputs}")

    list1, list2 = inputs  # Unpack the tuple

    sll1, sll2 = SinglyLinkedList(), SinglyLinkedList()  # Create two linked lists
    sll1.generate_list_from_array(list1)
    sll1.sort()  # Ensure both lists are sorted
    sll2.generate_list_from_array(list2)
    sll2.sort()

    merged_head = sll1.sorted_merge(sll1.get_head_node(), sll2.get_head_node())  # Merge

    # Convert the merged linked list back to an array
    merged_list = []
    current = merged_head
    while current:
        merged_list.append(current.data)
        current = current.next

    return merged_list

if __name__ == "__main__":

    test_cases = [
        (([], []), []),                     # 1: Merging two empty lists → []
        (([1], [1]), [1, 1]),               # 2: Merging [1] and [1] → [1, 1]
        (([1, 2], [1]), [1, 1, 2]),         # 3: Merging [1, 2] and [1] → [1, 1, 2]
        (([2, 1], [2, 1]), [1, 1, 2, 2]),   # 4: Merging [2, 1] and [2, 1] → [1, 1, 2, 2]
        (([3, 2, 1], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),  # 5: Merging [3, 2, 1] and [4, 5, 6] → [1, 2, 3, 4, 5, 6]
    ]

    run_sll_tests(SinglyLinkedList(), None, test_cases, merge_extractor)