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
        ([], 0),                           #  1. Empty list: No bars, area is 0.
        ([1], 1),                          #  2. Single bar: Area is bar height (1*1 = 1).
        ([1, 1, 1, 1, 1], 5),              #  3. Uniform bars: 1*5 = 5.
        ([1, 2, 3, 4, 5], 9),              #  4. Increasing bars: Maximum area is 9.
        ([5, 4, 3, 2, 1], 9),              #  5. Decreasing bars: Maximum area is also 9.
        ([2, 1, 5, 6, 2, 3], 10),          #  6. Mixed heights: Classic example yielding area 10.
        ([6, 2, 5, 4, 5, 1, 6], 12),       #  7. Another classic example yielding area 12.
        ([2, 4, 2, 1, 5, 6, 2, 3, 2], 10), #  8. Complex case yielding area 10.
        ([2, 2, 2, 2], 8)                  #  9. Uniform bars with height 2: 2*4 = 8.
    ]

    run_stack_tests(None, None, test_cases, largest_rectangle_extractor)
