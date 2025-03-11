from my_code.overviews._3_1_stack import Stack
from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests

# Test returning the max value in a stack

if __name__ == "__main__":

    test_cases = [
        ([], None),           #  1: Empty stack.
        ([1], 1),             #  2: Single item stack.
        ([1, 2], 2),          #  3: Two item stack.
        ([1, 2, 3], 3),       #  4: Multiple item stack.
        ([9, 1, 1, 1, 9], 9), #  5: Double item mixed stack.
    ]

    stack = Stack()
    run_stack_tests(stack, stack.max_value(), test_cases)