from my_code.overviews._2_1_doubly_linked_list import DoublyLinkedList
from my_code._2_1_doubly_linked_list_problems.dll_dynamic_test_function import run_dll_tests

# Test insertion of an item at the beginning of a singly linked list

def insert_into_sorted_extractor(dll, inputs):
    """ Extracts the result after inserting multiple items at the end. """
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for insert_at_end: {inputs}")
    
    initial_values, to_insert = inputs  # Unpack ([], (1, 2, 3))

    dll.generate_list_from_array(initial_values)  # Initialize list

    dll.sorted_insert(to_insert)

    return dll.to_array()  # Convert to array for comparison

if __name__ == "__main__":

    test_cases = [
        (([], 1), [1]),                 #  1: Inserting into an empty list.
        (([1], 2), [1, 2]),             #  2: Simple insert end.
        (([2], 1), [1, 2]),             #  3: Simple insert start.
        (([1, 2, 3], 4), [1, 2, 3, 4]), #  4: Simple insert end.
        (([1, 3, 5], 2), [1, 2, 3, 5]), #  5: Mixed insert.
        (([10, 20], 30), [10, 20, 30]), #  6: Double digits.
        (([7, 8, 9], 8), [7, 8, 8, 9]), #  7: Same number insert.
        (([0], 0), [0, 0]),             #  8: Zero insert.
        (([1000000, 2000000, 3000000],
           2500000), 
          [1000000, 2000000, 2500000, 3000000]), #  9: Large digits.
    ]


    dll = DoublyLinkedList()
    run_dll_tests(dll, None, test_cases, insert_into_sorted_extractor)
