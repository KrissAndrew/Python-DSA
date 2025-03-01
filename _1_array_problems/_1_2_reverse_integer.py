# While loop example
# Shift left and add last digit Ex 123. 
# 0 * 10 = 0 + 3 = 3 
# 3 * 10 = 30 + 2 = 32 
# 32 * 10 = 320 + 1 = 321 

def reverse_integer(n: int):
    if -10 < n < 10:  # Handles both positive and negative single-digit numbers
        return n
    
    result = 0
    sign = -1 if n < 0 else 1  # Store the sign separately
    n = abs(n)  # Work with absolute value

    while n > 0:
        result = result * 10 + (n % 10)  
        n //= 10  # Remove last digit

    return result * sign  # Reapply sign

if __name__ == "__main__":

    import sys
    import os

    # Add the parent directory to sys.path (Ensures Python finds `tests/`)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    # Now imports work!
    from tests.simple_python_test_structure import run_tests

    test_cases = [
        (1, 1),            # 1 Single digit
        (12, 21),          # 2 Two digits
        (123, 321),        # 3 Normal case
        (-123, -321),      # 4 Negative number
        (111114111111, 111111411111),  # 5 Large number
        (123456789, 987654321),  # 6 Large positive number
        (-123456789, -987654321),  # 7 Large negative number
        (0, 0),            # 8 Zero case
        (-1, -1),          # 9 Negative single digit
    ]

    run_tests(reverse_integer, test_cases)