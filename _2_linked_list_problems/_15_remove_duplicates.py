# Test sorting of a singly linked list 
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    sll = SinglyLinkedList()
    test_cases = [
        ([], Exception),                           #  1
        ([1], [1]),                                #  2
        ([1, 1], [1]),                             #  3
        ([1, 2, 2, 3], [1, 2, 3]),                 #  4
        ([1, 1, 2, 2, 3, 3, 4, 4], [1, 2, 3, 4]),  #  5
        ([5, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),     #  6
    ]

    all_passed = True
    sll = SinglyLinkedList()
    for i, (input, expected) in enumerate(test_cases, start=1):
        try:
            sll.generate_list_from_array(input)
            sll.remove_duplicates()
            result = sll.to_array()

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

    if all_passed:
        print("✅ All tests passed.")