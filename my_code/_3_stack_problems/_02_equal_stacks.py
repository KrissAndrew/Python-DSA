from my_code.overviews._3_1_stack import Stack
from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests

def equalise_stacks_extractor(inputs):
    """Equalise three stacks and return their common height.
    
    The stacks are provided as lists with the top on the left.
    This function builds a Stack for each list, reverses them
    (so the pop() method removes the 'top' element correctly),
    and iteratively pops from the tallest stack until all three 
    stacks have equal total height. If no equal height can be achieved,
    it returns 0.
    """
    if not isinstance(inputs, tuple) or len(inputs) != 3:
        raise ValueError(f"Invalid input format for linked list comparison: {inputs}")
    
    list1, list2, list3 = inputs  # Unpack the three stack lists
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    s1.generate_stack_from_array(list1)
    s2.generate_stack_from_array(list2)
    s3.generate_stack_from_array(list3)

    # Reverse stacks to account for the fact that the provided lists
    # have the top on the left. After reversing, pop() will remove
    # the top element correctly (i.e., from the right end).
    s1.reverse_stack()
    s2.reverse_stack()
    s3.reverse_stack()

    # Early exit cases
    # If the stacks are already equal, return the total immediately.
    if s1.total == s2.total == s3.total:
        return s1.total
    
    if any(total == 0 for total in [s1.total, s2.total, s3.total]):
        return 0

    # Iteratively pop from the stack with the highest total until all totals equalize.
    while not (s1.total == s2.total == s3.total):
        if s1.total >= s2.total and s1.total >= s3.total:
            s1.pop()
        elif s2.total >= s1.total and s2.total >= s3.total:
            s2.pop()
        else:
            s3.pop()

    # If the stack becomes empty, return 0.
    if not s1.stack: 
        return 0 
    return s1.total  # Return the common total height

if __name__ == "__main__":
    test_cases = [
        # Test Case 1: Already equal stacks.
        # All three stacks have the same total height (1+1+1 = 3), so no removals are necessary.
        (([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3),
        
        # Test Case 2: Example provided.
        # Stacks: 
        #   - [3, 2, 1, 1, 1]  (total = 8)
        #   - [4, 3, 2]        (total = 9)
        #   - [1, 1, 4, 1]     (total = 7)
        # After a series of removals, all stacks equalize at a height of 5.
        (([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]), 5),
        
        # Test Case 3: One empty stack.
        # When one of the stacks is empty, the only possible equal height is 0.
        (([], [1, 2, 3], [1, 1, 1]), 0),
        
        # Test Case 4: Multiple removals required.
        # Stacks: 
        #   - [3, 3, 3]          (total = 9)
        #   - [4, 2, 2, 2]       (total = 10)
        #   - [1, 1, 4, 1, 1]    (total = 8)
        # Removing the appropriate top elements leads to an equalized height of 6.
        (([3, 3, 3], [4, 2, 2, 2], [1, 1, 4, 1, 1]), 6),
        
        # Test Case 5: Large differences requiring full reduction.
        # Stacks: 
        #   - [1, 2, 3, 4, 5]  (total = 15)
        #   - [3, 3, 3, 3]     (total = 12)
        #   - [10]             (total = 10)
        # In this scenario, removals must continue until all stacks are reduced to 0.
        (([1, 2, 3, 4, 5], [3, 3, 3, 3], [10]), 0),
    ]

    # run_stack_tests executes the tests using our equalise_stacks_extractor function.
    # It compares the returned height with the expected height.
    run_stack_tests(None, None, test_cases, equalise_stacks_extractor)
