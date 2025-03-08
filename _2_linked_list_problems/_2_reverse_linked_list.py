# Tests for reversal of linked list
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    test_cases = [
        ([], Exception),             #  1
        ([1], [1]),                  #  2
        ([1, 2, 3], [3, 2, 1]),      #  3
        ([1, 2, 3, 4], [4, 3, 2, 1]) #  4
    ]

    all_passed = True
    ssl = SinglyLinkedList()
    for i, (inputs, expected) in enumerate(test_cases, start=1):
        try:
            # If inputs is a tuple, unpack it; otherwise, pass it as a single argument
            ssl.generate_list_from_array(*inputs) if isinstance(inputs, tuple) else ssl.generate_list_from_array(inputs)
            ssl.reverse_list()

            result = []
            for i in ssl:
                result.append(i.data)

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