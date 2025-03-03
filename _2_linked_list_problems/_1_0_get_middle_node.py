# Construct an in-place (without extra memory) algorithm to find and return the middle node of a linked list
# Must be O(N) (linear) running time
# Examples: [1, 2, 3, 4] --> middle node is: 2,   [1, 2, 3, 4, 5] --> middle node is: 3

# For the sake of this I will implement a find_middle_node() function in my linked list classes

if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList
    
    ssl = SinglyLinkedList()
    ssl.generate_list_from_array([])

    test_cases = [
        ([], Exception),          # 1
        ([1], 1),         # 2
        ([1, 2, 3], 2),   # 3
        ([1, 2, 3, 4], 2) # 4
    ]

    all_passed = True
    ssl = SinglyLinkedList()
    for i, (inputs, expected) in enumerate(test_cases, start=1):
        try:
            # If inputs is a tuple, unpack it; otherwise, pass it as a single argument
            ssl.generate_list_from_array(*inputs) if isinstance(inputs, tuple) else ssl.generate_list_from_array(inputs)
            result = ssl.get_middle_node().data
            if result != expected:
                all_passed = False
                print(f"❌ Test {i} Failed | Input: {inputs} | Expected: {expected}, Got: {result}")
        except Exception as e:
            if isinstance(expected, type) and issubclass(expected, Exception):
                if isinstance(e, expected):
                    continue
                else:
                    all_passed = False
                    print(f"❌ Test {i} Failed | Input: {inputs} | Expected Exception: {expected}, Got Exception: {type(e).__name__} - {e}")
            else:
                all_passed = False
                print(f"\n⚠️ Error in test {i} | Input: {inputs}")
                print(f"Exception: {e}")

    if all_passed:
        print("✅ All tests passed.")