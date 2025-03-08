# Palindrome - a word phrase or sequence that reads the same backwards and forwards
def is_palindrome(s: str) -> bool:
    if len(s) == 1 or len(s) == 0: 
        return True
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

from _1_0_reverse_in_place import reverse_in_place

def is_palindrome_reverse(s: str) -> bool:
    clean_s = "".join([c.lower() for c in s if c.isalnum()])
    return clean_s == reverse_in_place(clean_s)

if __name__ == "__main__":

    from tests.dynamic_test_function import run_tests

    test_cases = [
        # Basic cases
        ("racecar", True),                         #  1: Palindrome
        ("hello", False),                          #  2: Not a palindrome
        ("", True),                                #  3: Empty string is considered a palindrome
        ("a", True),                               #  4: Single character is always a palindrome
        
        # Cases with spaces and punctuation
        ("A man, a plan, a canal, Panama!", True), #  5: Famous palindrome with punctuation
        ("No 'x' in Nixon", True),                 #  6: Another palindrome with mixed case and punctuation
        ("Was it a car or a cat I saw?", True),    #  7: Contains spaces and question mark
        ("Eva, can I see bees in a cave?", True),  #  8: Mixed case, spaces, and punctuation

        # Cases with only non-alphanumeric characters
        ("!!!", True),                             #  9: Considered palindrome (since no real characters)
        ("12321", True),                           # 10: Numeric palindrome
        ("123421", False),                         # 11: Not a palindrome

        # Case sensitivity check
        ("AbBa", True),                            # 12: Should be case-insensitive
        
        # Edge cases
        ("a " * 5000 + "a", True),                 # 13: Large palindrome
        ("abcdefg" * 1000, False),                 # 14: Large non-palindrome
    ]

    run_tests(is_palindrome, test_cases)