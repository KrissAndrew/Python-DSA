from my_code.overviews._3_1_stack import Stack
from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests

# Test returning the max value in a stack

if __name__ == "__main__":


    test_cases = [
        ([], None),           #  1: Delete from empty list.
        ([1], 1),             #  2: Inserting into an empty list, invalid position
        ([1, 2], 2),          #  3: Delete multiple items.
        ([1, 2, 3], 3),       #  4: Delete central item multiple items into a non-empty list.
        ([9, 1, 1, 1, 9], 9), #  5: Delete multiple of same item.
    ]

    stack = Stack()
    run_stack_tests(stack, stack.max_value(), test_cases)