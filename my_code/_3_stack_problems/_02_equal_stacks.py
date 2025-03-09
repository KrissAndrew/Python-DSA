from my_code.overviews._3_1_stack import Stack
from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests

# Test in-place (without extra memory) return of middle node of a linked list
# Can extend the stack class to track max_values

def equalise_stacks_extractor(inputs):
    """Compares two linked lists and returns True if they are identical."""
    if not isinstance(inputs, tuple) or len(inputs) != 3:
        raise ValueError(f"Invalid input format for linked list comparison: {inputs}")
    
    list1, list2, list3 = inputs  # Unpack (list1, list2)

    s1, s2, s3 = Stack(), Stack(), Stack()  # Create two linked lists
    s1.generate_stack_from_array(list1)
    s2.generate_stack_from_array(list2)
    s3.generate_stack_from_array(list3)

    # Stack equalisation logic here
    

    return sum(s1.stack) == sum(s2.stack) == sum(s3.stack)  # Compare the lists

if __name__ == "__main__":

    test_cases = [
        (([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]), None),           #  1: Delete from empty list.
        # ([1], 1),             #  2: Inserting into an empty list, invalid position
        # ([1, 2], 2),          #  3: Delete multiple items.
        # ([1, 2, 3], 3),       #  4: Delete central item multiple items into a non-empty list.
        # ([9, 1, 1, 1, 9], 9), #  5: Delete multiple of same item.
    ]

    stack = Stack()
    run_stack_tests(stack, stack.max_value(), test_cases)