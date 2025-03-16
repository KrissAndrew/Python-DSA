from my_code._3_stack_problems.stack_dynamic_test_function import run_stack_tests

def largest_rectangle_extractor(heights):
    """Given an array representing heights, return the area of the largest rectangle possible."""
    if not isinstance(heights, list):
        raise ValueError(f"Invalid heights format (list required) for largest_rectangle: {heights}")
    
    if not heights:
        return 0
    if len(set(heights)) == 1 or len(heights) == 1:
        return len(heights) * heights[0]
    
    max_area = 0
    stack = []

    for i, height in enumerate(heights):
        # When the current bar is less than the last bar in the stack, pop from the stack.
        while stack and height < heights[stack[-1]]:
            top_index = stack.pop()
            # Compute width: if stack is empty, width = i; else, width = i - stack[-1] - 1.
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top_index] * width)
        stack.append(i)
    
    # Process remaining bars in the stack
    while stack:
        top_index = stack.pop()
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[top_index] * width)
    
    return max_area


if __name__ == "__main__":

    test_cases = [
        ([], 0),                                                #  1: Empty list, max area is 0
        ([1], 1),                                               #  1: Single item input, max area is height of only item
        ([1, 1, 1, 1, 1], 5),                                   #  1: Even height, max area is from 1 onwards for 1 * 5 = 9
        ([1, 2, 3, 4, 5], 9),                                   #  1: Max rectangular area is from 3 onwards for 3 * 3 = 9
        ([5, 6, 7, 8, 9], 25),                                  #  1: Max rectangular area is from 3 onwards for 3 * 3 = 9
        # (([1], [], 1), 1),                                    #  2: One element equals maxSum, one move from stack A.
        # (([2], [], 1), 0),                                    #  3: Single element exceeds maxSum, no moves allowed.
        # (([1, 2, 3], [], 4), 2),                              #  4: Only stack A available; only two moves before exceeding maxSum.
        # (([4, 2, 4, 6, 1], [2, 1, 8, 5], 10), 4),             #  5: Mixed stacks; optimal combination yields 4 moves.
        # (([3, 3, 3, 3, 3], [3, 3, 3, 3, 3], 12), 4),          #  6: Uniform stacks (all 3's); only 4 moves possible.
        # (([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 10), 10),         #  7: All ones; maximum moves equal total number of ones (10 moves).
        # (([7, 5, 3], [7, 5, 3], 15), 3),                      #  8: High values in both stacks; only a few moves possible.
        # (([5, 6, 7], [1, 2, 3, 4], 10), 4),                   #  9: Different stack magnitudes; optimal strategy takes all from stack B.
        # (([4, 2, 4, 6, 1, 1, 2], [2, 1, 8, 5, 3, 1], 20), 7)  # 10: Complex case; mixing pops from both stacks yields 7 moves.
    ]

    run_stack_tests(None, None, test_cases, largest_rectangle_extractor)
