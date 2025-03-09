from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import run_sll_tests

def get_at_position_extractor(sll, inputs):
    """Extracts the node at the given position."""
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for get_node_at_position: {inputs}")
    
    array, position = inputs  # Unpack ([initial_list], (position,))
    position = position[0]  # ✅ Convert tuple to int

    sll.generate_list_from_array(array)  # Initialize list

    return sll.get_node_at_position(position)  # ✅ Pass correct integer position

if __name__ == "__main__":

    test_cases = [
        (([], (9,)), Exception),         # 1: Get from empty list.
        (([1], (1,)), SinglyLinkedList.Node(1)),  # 2: Get first node.
        (([1, 2], (2,)), SinglyLinkedList.Node(2)),  # 3: Get second node.
        (([1, 9, 3], (2,)), SinglyLinkedList.Node(9)),  # 4: Get middle node.
        (([9, 1, 1, 1, 9], (1,)), SinglyLinkedList.Node(9)),  # 5: Get first node.
    ]

    run_sll_tests(SinglyLinkedList(), None, test_cases, get_at_position_extractor)
