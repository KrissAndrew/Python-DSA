# Test insertion of an item at the start of a singly linked list 
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    test_cases = [
        ([], Exception),                                           #  1
        ([1], [1]),                                                #  2
        ([1, 2], [2, 1]),                                          #  3
        ([1, 2, 3], [3, 2, 1]),                                    #  4
        ([1, 3, 89, 12, 189, 200098], [200098, 189, 12, 89, 3, 1]) #  5
    ]

    all_passed = True
    sll = SinglyLinkedList()
    for i, (inputs, expected) in enumerate(test_cases, start=1):
        try:
            # If inputs is a tuple, unpack it; otherwise, pass it as a single argument
            sll.generate_list_from_array(*inputs) if isinstance(inputs, tuple) else sll.generate_list_from_array(inputs)
            sll.reverse_list()
            result = sll.to_array()

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