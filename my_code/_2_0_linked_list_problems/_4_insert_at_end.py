from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import sll_run_tests

def insert_at_end_extractor(sll, inputs):
    """ Extracts the result after inserting multiple items at the end. """
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for insert_at_end: {inputs}")
    
    initial_values, to_insert = inputs  # Unpack ([], (1, 2, 3))

    sll.generate_list_from_array(initial_values)  # Initialize list

    for num in to_insert:  # Insert multiple items at the end
        sll.insert_at_end(num)

    return sll.to_array()  # Convert to array for comparison

if __name__ == "__main__":
    
    test_cases = [
        (([], (1,)), [1]),                                # Case 1: Inserting into an empty list.
        (([1], (2, 3)), [1, 2, 3]),                       # Case 2: Inserting multiple items into a non-empty list.
        (([1, 2, 3], (4, 5)), [1, 2, 3, 4, 5]),           # Case 3: Appending two items.
        (([1, 2, 3, 4], (5,)), [1, 2, 3, 4, 5]),          # Case 4: Appending a single item.
        (([10, 20], (30, 40, 50)), [10, 20, 30, 40, 50]), # Case 5: Appending three items to a short list.
        (([7, 8, 9], ()), [7, 8, 9]),                     # Case 6: No items to append (list remains unchanged).
        (([0], (0, 0, 0)), [0, 0, 0, 0]),                 # Case 7: Appending multiple zeros.
        (([], (5, 6, 7)), [5, 6, 7]),                     # Case 8: Starting with an empty list and appending several items.
        (([100], (200,)), [100, 200]),                    # Case 9: Single-item list with one appended item.
        (([1, 3, 5], (2, 4, 6)), [1, 3, 5, 2, 4, 6])      # Case 10: Appending to an odd-length list.
    ]

    sll = SinglyLinkedList()
    print("Running tests for insert_at_end()...")
    sll_run_tests(sll, None, test_cases, insert_at_end_extractor)