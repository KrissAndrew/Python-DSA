from my_code.overviews._3_1_stack import Stack
from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests

def game_of_two_stacks_extractor(inputs):
    """Given two stacks and a maximum number, return the highest number of pop methods
       possible to call on the stacks without the popped values exceeding the max_number
    """
    if not isinstance(inputs, tuple) or len(inputs) != 3:
        raise ValueError(f"Invalid input format for linked list comparison: {inputs}")
    
    list1, list2, max_pop = inputs  # Unpack (list1, list2, list3)
    s1 = Stack()
    s2 = Stack()
    s1.generate_stack_from_array(list1)
    s2.generate_stack_from_array(list2)

    # Reverse stacks to account for the fact that the provided lists
    # have the top on the left. After reversing, pop() will remove
    # the top element correctly (i.e., from the right end).
    s1.reverse_stack()
    s2.reverse_stack()

    s1_cumulative, s2_cumulative = [], []

    while s1.total >= max_pop:
        s1_cumulative.append(s1.pop())
    
    for i in range(1, len(s1_cumulative)):
        if s1_cumulative[i - 1] + s1_cumulative[i] <= max_pop:
            s1_cumulative[i] = s1_cumulative[i - 1] + s1_cumulative[i]

    while s2.total >= max_pop:
        s2_cumulative.append(s2.pop())

    for i in range(1, len(s2_cumulative)):
        if s2_cumulative[i - 1] + s2_cumulative[i] <= max_pop:
            s2_cumulative[i] = s2_cumulative[i - 1] + s2_cumulative[i]

    
if __name__ == "__main__":

    test_cases = [
        (([4, 2, 4, 6, 1], [2, 1, 8, 5], 10), 4),           #  1: Delete from empty list.
        # ([1], 1),             #  2: Inserting into an empty list, invalid position
        # ([1, 2], 2),          #  3: Delete multiple items.
        # ([1, 2, 3], 3),       #  4: Delete central item multiple items into a non-empty list.
        # ([9, 1, 1, 1, 9], 9), #  5: Delete multiple of same item.
    ]

    stack = Stack()
    run_stack_tests(None, None, test_cases, game_of_two_stacks_extractor)