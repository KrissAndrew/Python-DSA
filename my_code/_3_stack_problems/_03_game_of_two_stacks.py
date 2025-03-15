def game_of_two_stacks_extractor(inputs):
    """Given two stacks (represented as lists) and a maximum sum, return the maximum number of pop operations
       (from the top of either stack) such that the cumulative sum of popped values does not exceed max_pop.
    """
    if not isinstance(inputs, tuple) or len(inputs) != 3:
        raise ValueError(f"Invalid input format for game_of_two_stacks: {inputs}")
    
    list1, list2, max_pop = inputs  # Unpack (list1, list2, max_pop)

    # Initialize the running sum and pointers for each stack
    sum_ = 0
    p1, p2 = 0, 0
    max_count = 0

    # **Fix in Initial Accumulation from list1:**
    # We add an element only if it does not cause the sum to exceed max_pop.
    while p1 < len(list1) and sum_ + list1[p1] <= max_pop:
        sum_ += list1[p1]
        p1 += 1

    # max_count is the number of moves possible using only stack A.
    max_count = p1

    # Now, iterate over stack B (list2) and try to include elements from it.
    while p2 < len(list2):
        # Add the next element from stack B.
        sum_ += list2[p2]
        p2 += 1

        # If the sum exceeds max_pop, try to remove some elements from list1
        while sum_ > max_pop and p1 > 0:
            p1 -= 1
            sum_ -= list1[p1]

        # If the current sum is within the limit, update max_count.
        if sum_ <= max_pop:
            max_count = max(max_count, p1 + p2)
        else:
            # If even after removing all elements from list1 the sum exceeds max_pop, break.
            break
    
    return max_count

if __name__ == "__main__":

    test_cases = [
        (([], [], 10), 0),                                    #  1: Both stacks empty, no moves possible.
        (([1], [], 1), 1),                                    #  2: One element equals maxSum, one move from stack A.
        (([2], [], 1), 0),                                    #  3: Single element exceeds maxSum, no moves allowed.
        (([1, 2, 3], [], 4), 2),                              #  4: Only stack A available; only two moves before exceeding maxSum.
        (([4, 2, 4, 6, 1], [2, 1, 8, 5], 10), 4),             #  5: Mixed stacks; optimal combination yields 4 moves.
        (([3, 3, 3, 3, 3], [3, 3, 3, 3, 3], 12), 4),          #  6: Uniform stacks (all 3's); only 4 moves possible.
        (([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 10), 10),         #  7: All ones; maximum moves equal total number of ones (10 moves).
        (([7, 5, 3], [7, 5, 3], 15), 3),                      #  8: High values in both stacks; only a few moves possible.
        (([5, 6, 7], [1, 2, 3, 4], 10), 4),                   #  9: Different stack magnitudes; optimal strategy takes all from stack B.
        (([4, 2, 4, 6, 1, 1, 2], [2, 1, 8, 5, 3, 1], 20), 7)  # 10: Complex case; mixing pops from both stacks yields 7 moves.
    ]

    from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests
    run_stack_tests(None, None, test_cases, game_of_two_stacks_extractor)
