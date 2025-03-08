
# Can extend the stack class to track max_values

if __name__ == "__main__":

    from overviews._3_1_stack import Stack

    test_cases = [
        ([], None),      #  1: Delete from empty list.
        ([1], 1),             #  2: Inserting into an empty list, invalid position
        ([1, 2], 2),          #  3: Delete multiple items.
        ([1, 2, 3], 3),       #  4: Delete central item multiple items into a non-empty list.
        ([9, 1, 1, 1, 9], 9), #  5: Delete multiple of same item.
    ]

    all_passed = True
    stack = Stack()
    for i, (input, expected) in enumerate(test_cases, start=1):
        try:
            stack.generate_stack_from_array(input)
            result = stack.max_value()

            if result != expected:
                all_passed = False
                print(f"❌ Test {i} Failed | Input: {input} | Expected: {expected}, Got: {result}")
        except Exception as e:
            if isinstance(expected, type) and issubclass(expected, Exception):
                if isinstance(e, expected):
                    continue
                else:
                    all_passed = False
                    print(f"❌ Test {i} Failed | Input: {input} | Expected Exception: {expected}, Got Exception: {type(e).__name__} - {e}")
            else:
                all_passed = False
                print(f"\n⚠️ Error in test {i} | Input: {input}")
                print(f"Exception: {e}")

    # Test case with removal of items
    all_passed = True
    stack = Stack()
    stack.generate_stack_from_array([1, 2, 3, 4, 5])
    stack.pop()
    result = stack.max_value()
    expected = 4

    if result != expected:
        all_passed = False
        print(f"❌ Test Failed | Input: {input} | Expected: {expected}, Got: {result}")

        all_passed = True

    
    stack = Stack()
    stack.generate_stack_from_array([1, 2, 3, 4, 5, 5, 5, 5])
    for _ in range(5):
        stack.pop()
    result = stack.max_value()
    expected = 3

    if result != expected:
        all_passed = False
        print(f"❌ Test Failed | Input: {input} | Expected: {expected}, Got: {result}")

    if all_passed:
        print("✅ All tests passed.")