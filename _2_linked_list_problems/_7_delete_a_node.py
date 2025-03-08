# Test insertion of an item at the start of a singly linked list 
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    test_cases = [
        ([], (9,), Exception),                                         #  1: Delete from empty list.
        ([1], (1,), []),                                               #  2: Inserting into an empty list, invalid position
        ([1, 2], (1, 2), []),                                          #  3: Delete multiple items.
        ([1, 2, 3], (2,), [1, 3]),                                     #  4: Delete central item multiple items into a non-empty list.
        ([9, 1, 1, 1, 9], (1, 1, 1), [9, 9]),                             #  5: Delete multiple of same item.
    ]

    all_passed = True
    sll = SinglyLinkedList()
    for i, (array, inserts, expected) in enumerate(test_cases, start=1):
        try:
            sll.generate_list_from_array(array)

            for number in inserts:
                sll.delete_first_occurance(number)

            result = sll.to_array()

            if result != expected:
                all_passed = False
                print(f"❌ Test {i} Failed | Input: {inserts} | Expected: {expected}, Got: {result}")
        except Exception as e:
            if isinstance(expected, type) and issubclass(expected, Exception):
                if isinstance(e, expected):
                    continue
                else:
                    all_passed = False
                    print(f"❌ Test {i} Failed | Input: {inserts} | Expected Exception: {expected}, Got Exception: {type(e).__name__} - {e}")
            else:
                all_passed = False
                print(f"\n⚠️ Error in test {i} | Input: {inserts}")
                print(f"Exception: {e}")

    if all_passed:
        print("✅ All tests passed.")