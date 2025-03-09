from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import run_sll_tests

# Test insertion of an item at the provided position within a singly linked list 

def insert_at_position_extractor(sll, inputs):
    """Extracts the result after inserting multiple items at specified positions."""
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for insert_at_position: {inputs}")
    
    array, inserts = inputs  # Unpack ([initial_list], ((value, position), ...))

    sll.generate_list_from_array(array)  # Initialize list

    for number, position in inserts:  # Insert at given positions
        sll.insert_at_position(number, position)

    return sll.to_array()  # Convert to array for comparison

if __name__ == "__main__":
    
    test_cases = [
        (([], ((9,1),)), [9]),                                           #  1: Inserting into an empty list.
        (([], ((9,2),)), Exception),                                     #  2: Inserting into an empty list, invalid position.
        (([1], ((2, 1),)), [2, 1]),                                      #  3: Inserting multiple items into a non-empty list.
        (([1], ((2, 2),)), [1, 2]),                                      #  4: Inserting multiple items into a non-empty list.
        (([1, 2, 3, 4], ((9, 3),)), [1, 2, 9, 3, 4]),                    #  5: Insert in middle.
        (([10, 20], ((30, 1), (40, 4), (50, 2))), [30, 50, 10, 20, 40]), #  6: Inserting three items to a short list.
        (([7, 8, 9], ()), [7, 8, 9]),                                    #  7: No items to append (list remains unchanged).
        (([0], ((0, 1), (0, 1), (0, 1))), [0, 0, 0, 0]),                 #  8: Appending multiple zeros.
        (([], ((5, 1), (6, 2), (7, 3))), [5, 6, 7]),                     #  9: Starting with an empty list and appending several items.
    ]

    sll = SinglyLinkedList()
    run_sll_tests(sll, None, test_cases, insert_at_position_extractor)
