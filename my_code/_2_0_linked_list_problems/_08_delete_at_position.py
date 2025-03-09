from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import sll_run_tests

# Test deletion of an item at the provided position within a singly linked list 

def delete_at_position_extractor(sll, inputs):
    """Extracts the result after deleting item/s at specified positions."""
    if not isinstance(inputs, tuple) or len(inputs) != 2:
        raise ValueError(f"Invalid input format for delete_at_position: {inputs}")
    
    array, positions = inputs  # Unpack ([initial_list], ((position,), ...))

    sll.generate_list_from_array(array)  # Initialize list

    for position in positions:  # Delete at given positions
        sll.delete_at_position(position[0])  # Extract single integer from tuple

    return sll.to_array()  # Convert to array for comparison

if __name__ == "__main__":

    test_cases = [
        (([], ((1,),)), Exception),               # 1: Deleting from empty list.
        (([9], ((1,),)), []),                     # 2: Delete item at first position 
        (([1, 2], ((1,), (1,))), []),             # 3: Delete multiple items.
        (([1, 2, 3], ((1,), (2,))), [2]),         # 4: Delete outer items.
        (([1, 2, 3, 4], ((2,), (2,))), [1, 4]),   # 5: Delete multiple items from middle.
    ]

    sll = SinglyLinkedList()
    sll_run_tests(sll, None, test_cases, delete_at_position_extractor)
