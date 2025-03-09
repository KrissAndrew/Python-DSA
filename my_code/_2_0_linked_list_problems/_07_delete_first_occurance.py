from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import run_sll_tests

# Test deletion of the first occurance of the provided item in a singly linked list 

def delete_first_occurance_extractor(sll, inputs):
    """ Extracts the result after inserting multiple items at the end. """
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for insert_at_end: {inputs}")
    
    initial_values, to_delete = inputs  # Unpack ([], (1, 2, 3))

    sll.generate_list_from_array(initial_values)  # Initialize list

    for num in to_delete:  # delete multiple occurances of items
        sll.delete_first_occurance(num)

    return sll.to_array()  # Convert to array for comparison

# Test insertion of an item at the start of a singly linked list 
if __name__ == "__main__":

    test_cases = [
        (([], (9,)), Exception),                                         #  1: Delete from empty list.
        (([1], (1,)), []),                                               #  2: Inserting into an empty list, invalid position
        (([1, 2], (1, 2)), []),                                          #  3: Delete multiple items.
        (([1, 2, 3], (2,)), [1, 3]),                                     #  4: Delete central item multiple items into a non-empty list.
        (([9, 1, 1, 1, 9], (1, 1, 1)), [9, 9]),                             #  5: Delete multiple of same item.
    ]

    all_passed = True
    sll = SinglyLinkedList()
    run_sll_tests(sll, None, test_cases, delete_first_occurance_extractor)