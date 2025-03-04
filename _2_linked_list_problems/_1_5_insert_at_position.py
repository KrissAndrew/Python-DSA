# Test insertion of an item at the start of a singly linked list 
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    test_cases = [
        ([], ((9,1),), [9]),                                           #  1: Inserting into an empty list.
        ([], ((9,2),), Exception),                                     #  2: Inserting into an empty list, invalid position
        ([1], ((2, 1),), [2, 1]),                                      #  3: Inserting multiple items into a non-empty list.
        ([1], ((2, 2),), [1, 2]),                                      #  4: Inserting multiple items into a non-empty list.
        ([1, 2, 3, 4], ((9, 3),), [1, 2, 9, 3, 4]),                    #  5: Insert in middle.
        ([10, 20], ((30, 1), (40, 4), (50, 2)), [30, 50, 10, 20, 40]), #  6: Inserting three items to a short list.
        ([7, 8, 9], (), [7, 8, 9]),                                    #  7: No items to append (list remains unchanged).
        ([0], ((0, 1), (0, 1), (0, 1)), [0, 0, 0, 0]),                 #  8: Appending multiple zeros.
        ([], ((5, 1), (6, 2), (7, 3)), [5, 6, 7]),                     #  9: Starting with an empty list and appending several items.
    ]

    all_passed = True
    sll = SinglyLinkedList()
    for i, (array, inserts, expected) in enumerate(test_cases, start=1):
        try:
            sll.generate_list_from_array(array)

            for number, position in inserts:
                sll.insert_at_position(number, position)

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