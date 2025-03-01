# Anagram - jumbled words with the same number of characters ANAGRAM - NAGARAM
# Frequencies matter, but order does not.
# This is a primary example of using a lists O(1) item access to its fullest potential

def valid_anagram(string1: str, string2: str) -> bool:
    counts = [0] * 36 # 26 letters + 10 digits

    for c in string1:
        if c.isalpha():
            counts[ord(c.lower()) - ord('a')] += 1
        elif c.isdigit():
            counts[ord(c) - ord('0') + 26] += 1
    
    for c in string2:
        if c.isalpha():
            counts[ord(c.lower()) - ord('a')] -= 1
        elif c.isdigit():
            counts[ord(c) - ord('0') + 26] -= 1
    
    return all(count == 0 for count in counts)

if __name__ == "__main__":

    import sys
    import os

    # Add the parent directory to sys.path (Ensures Python finds `tests/`)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    # Now imports work!
    from tests.simple_python_test_structure import run_tests

    test_cases = [
        # Basic Anagrams
        (("listen", "silent"), True),           # 1
        (("test", "etts"), True),               # 2
        (("anagram", "nagaram"), True),         # 3
        (("rat", "tar"), True),                 # 4

        # Anagrams with Numbers
        (("abc123", "bca321"), True),           # 5
        (("112233", "321132"), True),           # 6
        (("12a3b4", "4b3a21"), True),           # 7

        # Not Anagrams
        (("abc123", "abc124"), False),          # 8 One digit is different
        (("112233", "112334"), False),          # 9 Different frequency of digits

        # Case Insensitivity
        (("Listen123", "Silent321"), True),     # 10
        (("Hello2022", "oLleh2202"), True),     # 11

        # Spaces & Punctuation Ignored
        (("Dormitory 123", "Dirty room 321"), True),  # 12
        (("Tom Marvolo Riddle 42", "I am Lord Voldemort 24"), True),  # 13

        # Different Lengths (Immediate Fail)
        (("aa", "aaa"), False),                 # 14
        (("", "a"), False),                     # 15
    ]
    
    run_tests(valid_anagram, test_cases)