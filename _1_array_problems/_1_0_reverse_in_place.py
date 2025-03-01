# Time Complexity: O(n) - unsorted list reversal will always need to visit all elements
# Space Complexity: O(1) Benefit of pointers

from typing import Union

def reverse_in_place(data: Union[list[int], str]) -> Union[list[int], str]:
    if isinstance(data, str):
        # Convert to a list for in-place modification
        data = list(data)
        is_string = True
    else:
        is_string = False
    
    # Two-pointer swap logic (works for lists)
    left, right = 0, len(data) - 1
    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    # Convert back to string if the input was a string
    return "".join(data) if is_string else data

if __name__ == "__main__":
    from tests.dynamic_test_function import run_tests

    test_cases = [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [3, 2, 1]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 1], [1, 1, 1])
    ]

    run_tests(reverse_in_place, test_cases)
