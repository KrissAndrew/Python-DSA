### ARRAYS ###
# In python arrays are known as lists
# lists are mutable data structures, their content can be changed in place.

# When a python list is created, it is automatically allocated a chunk of contiguous memory
# If this memory is exceeded, it will increase the list size by a multiple of the original (1.5)
# Python lists are unique - they store reference objects which point to the location of each object in the array

# List time complexities
# Search
# Known index O(1) - Primary benefit of arrays are their fast individual access
# Arbitrary index O(n) - May have to search all items
# Insert
# Insert an item O(n) - at the worst case (first item) all items must be shifted
# Insert item at end O(1) - Fast to add an item to the end
# Delete
# Delete item O(n) - as above, all items may need to shift (first item)
# Delete item at end O(n) - as above,  Fast to add an item to the end


# Indexing & Slicing:
# You can access elements by index, and slicing lets you work with sublists.
print("\nList slicing")
arr = [10, 20, 30, 40, 50]
print(arr)
print(arr[2])      # Output: 30
print(arr[1:4])    # Output: [20, 30, 40] - python strings are [inclusive:exclusive] unless the end is blank
print(arr[::-1])   # Output: [50, 40, 30, 20, 10]


# Iteration:
# Looping through lists is straightforward.
print("\nTraverse list with index using enumerate")
for i, value in enumerate(arr):
    print(f"Index {i}: {value}")


# Modification:
# lists are mutable, you can update elements, append new ones, or remove them.
arr[2] = 35     # Update element
arr.append(60)  # Append new element
arr.pop()       # Remove last item
arr.remove(20)  # Remove first occurrence of 20
arr.extend(arr)
print(arr)
arr.reverse()   # Reverse list
print(arr)
arr.sort()      # Sort the list
print(arr)

# List Comprehensions:
# List Comprehensions offer a concise way to create or transform arrays.
print('\nList Comprehension')
squared = [x ** 2 for x in arr]
print(squared)

# Filter even numbers
evens_arr = [1, 2, 3, 4, 5, 6]
evens = [x for x in evens_arr if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]

# Matrices
# 2d and 3d lists can be confusing to deal with, and iterating over them can lead to large time complexities.
print('\nMatrices')
rows, cols = 4, 3
matrix = [[0] * cols for _ in range(rows)]
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = j

print(matrix)

# row by row processing
print('\nMatrix row by row')
for row in matrix:
    print(row)

print('\nMatrix element by element')
# Item by item
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
    print()

# Using List Comprehension (Flattening a Matrix)
flattened = [element for row in matrix for element in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Iterating Column-Wise (zip())
print("\nColumns extraction")
for col in zip(*matrix):
    print(col)

print("\nUnintended object modification")
# since lists store references to objects, altering data without realising is possible
matrix_end_half = matrix[len(matrix) // 2:]
print(matrix_end_half)
print(matrix) # Note how the original matrix has had its value altered

matrix_end_half[0][0] = 'Altered'
print(matrix_end_half)
print(matrix) # Note how the original matrix has had its value altered
matrix_end_half[0][0] = 0
print(matrix_end_half)
print(matrix) # Note how the original matrix has had its value altered

import copy
print("\nDeep copy approach")
matrix_copy = copy.deepcopy(matrix)
matrix_end_half = matrix_copy[len(matrix_copy) // 2:]
matrix_end_half[0][0] = 'Altered'
print(matrix_end_half)
print(matrix) # The original matrix remains the same


# Algorithmic Approaches:
# Two-Pointers/Sliding Window:
# Many array problems (e.g., finding a pair that sums to a target) can be approached with two pointers or sliding windows.

# Example: Find two numbers that sum to a given value (assuming a sorted array):
def find_pair(int_list, target):
    left, right = 0, len(int_list) - 1
    while left < right:
        current_sum = int_list[left] + int_list[right]
        if current_sum == target:
            return int_list[left], int_list[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

print(find_pair([1, 3, 4, 5, 7, 10], 9))  # Output (4, 5)


### STRINGS ###
# Python strings are immutable - any logic appearing to modify a string is creating a new one
print("\n\n")
# Indexing & Slicing:
# Similar to lists, you can use indexing and slicing to work with substrings.

s = "Hello, World!"
print(s[0])      # Output: H
print(s[7:12])   # Output: World
print(s[::-1])   # Output: !dlroW ,olleH (reversed string)


# Concatenation & Formatting:
# Use the + operator or formatted strings.

greeting = "Hello"
name = "Alice"
print(greeting + ", " + name + "!")  # Output: Hello, Alice!
# Or using f-string (Python 3.6+)
print(f"{greeting}, {name}!")


# Built-in String Methods:
# Python strings have many useful methods:

text = "  Python is fun!  "
print(text.strip())        # Removes leading/trailing whitespace
print(text.lower())        # Converts to lowercase
print(text.replace("fun", "awesome"))
print(text.split())        # Splits on whitespace by default


# Remove non-alphanumerical chars from a string
import re
s = "Hello, World! 123"
# This pattern matches any character that is not a letter (a-z or A-Z) or a digit (0-9)
clean_s = re.sub(r'[^a-zA-Z0-9]', '', s) # Substitute anything that is not in our pattern with ''
print(clean_s)  # Output: HelloWorld123

s = "Hello, World! 123"
clean_s = ''.join([char for char in s if char.isalnum()])
print(clean_s)  # Output: HelloWorld123

# Building Strings:
# Since strings are immutable, concatenating them in a loop can be inefficient because it creates many temporary objects.
# Instead, collect pieces in a list and use .join().

parts = ''
# Bad - a new string object is created for every iteration
for i in range(5):
    parts += str(i)

parts = []
# Good - a single parts list object is used
for i in range(5):
    parts.append(str(i))

result = "".join(parts)
print(result)  # Output: 01234

# Conversion between Strings and Lists:
# When performing multiple modifications (like character replacements), converting the string to a list of characters, modifying it, and then joining it back is a common approach.

s = "hello"
char_list = list(s)
char_list[0] = "H"
s = "".join(char_list)
print(s)  # Output: Hello


# simple way to determine if a word contains duplicate characters - compare len of word and len of set of word
duplicate = "aba"
non_duplicate = "abc"

def contains_duplicate(word):
    return len(set(word)) == len(word)

if contains_duplicate(duplicate):
    print(f"The word {duplicate} contains duplicate characters")
if not contains_duplicate(non_duplicate):
    print(f"The word {non_duplicate} does not contain duplicate characters")




# Anagram - jumbled words with the same number of characters ANAGRAM - NAGARAM
# Dealing with anagrams introduces the problem of multiple characters being important
# Due to this, sets cannot work for quick comparisons
# Counts now matter
from collections import Counter
anagram = "anagram"
nagaram = "nagaram"
if Counter(anagram) == Counter(nagaram):
    print(f"'{anagram}' is an anagram of '{nagaram}' identified via identical character counts")


# Palindrome - a word phrase or sequence that reads the same backwards and forwards
# For palindromes order matters. Due to this, you cannot simply compare counts.
# You can compare the first half to the back half 
s = "aabbaa!"
clean_s = ''.join([char.lower() for char in s if char.isalnum()]) # remove all non-alphanumeric items from string whilst lowering
print(clean_s[:len(clean_s) // 2] == clean_s[::-1][:len(clean_s) // 2])