# Test insertion of an item at the start of a singly linked list 
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    sll = SinglyLinkedList()
    test_cases = [
        ([], []),          #  1
        ([1], [1]),        #  2
        ([2, 1], [1, 2]), #  3
        ([1, 2, 3], []),  #  4
    ]

    all_passed = True
    sll = SinglyLinkedList()
    for i, (inputs, expected) in enumerate(test_cases, start=1):
        try:
            sll.generate_list_from_array(inputs[0])
            result = 0

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