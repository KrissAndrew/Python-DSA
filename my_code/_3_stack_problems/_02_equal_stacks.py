from my_code.overviews._3_1_stack import Stack
from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests

def equalise_stacks_extractor(inputs):
    """Equalise three stacks (lists with top on left) by removing elements from the tallest 
       until all stacks have the same height. Returns the common height or 0 if not possible.
    """
    if not isinstance(inputs, tuple) or len(inputs) != 3:
        raise ValueError(f"Invalid input format for equalise_stacks: {inputs}")
    
    list1, list2, list3 = inputs  # Unpack three stacks
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    s1.generate_stack_from_array(list1)  # Build stack from list1
    s2.generate_stack_from_array(list2)  # Build stack from list2
    s3.generate_stack_from_array(list3)  # Build stack from list3

    # Reverse stacks so pop() removes the correct top element
    s1.reverse_stack()
    s2.reverse_stack()
    s3.reverse_stack()

    # If stacks are already equal, return the height immediately
    if s1.total == s2.total == s3.total:
        return s1.total

    # If any stack is empty, equal height can't be achieved
    if any(total == 0 for total in [s1.total, s2.total, s3.total]):
        return 0

    # Remove top elements from the tallest stack until all totals equalize
    while not (s1.total == s2.total == s3.total):
        if s1.total >= s2.total and s1.total >= s3.total:
            s1.pop()
        elif s2.total >= s1.total and s2.total >= s3.total:
            s2.pop()
        else:
            s3.pop()

    # Return 0 if the stack is empty; otherwise, return the common height
    if not s1.stack: 
        return 0 
    return s1.total

if __name__ == "__main__":

    test_cases = [
        (([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3),           #  1: Already equal stacks (total 3)
        (([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]), 5),  #  2: Equalise to 5 after removals
        (([], [1, 2, 3], [1, 1, 1]), 0),                  #  3: One empty stack yields 0
        (([3, 3, 3], [4, 2, 2, 2], [1, 1, 4, 1, 1]), 6),  #  4: Equalise to 6 after several removals
        (([1, 2, 3, 4, 5], [3, 3, 3, 3], [10]), 0),       #  5: Removals reduce stacks to 0
    ]

    # Run tests using equalise_stacks_extractor
    run_stack_tests(None, None, test_cases, equalise_stacks_extractor)
