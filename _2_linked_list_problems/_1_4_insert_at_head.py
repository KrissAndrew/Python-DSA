# Test insertion of an item at the start of a singly linked list 
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    test_cases = [
        ([], (1,), [1]),                                #  1: Inserting into an empty list.
        ([1], (2, 3), [3, 2, 1]),                       #  2: Inserting multiple items into a non-empty list.
        ([1, 2, 3], (4, 5), [5, 4, 1, 2, 3]),           #  3: Appending two items.
        ([1, 2, 3, 4], (5,), [5, 1, 2, 3, 4]),          #  4: Appending a single item.
        ([10, 20], (30, 40, 50), [50, 40, 30, 10, 20]), #  5: Appending three items to a short list.
        ([7, 8, 9], (), [7, 8, 9]),                     #  6: No items to append (list remains unchanged).
        ([0], (0, 0, 0), [0, 0, 0, 0]),                 #  7: Appending multiple zeros.
        ([], (5, 6, 7), [7, 6, 5]),                     #  8: Starting with an empty list and appending several items.
        ([100], (200,), [200, 100]),                    #  9: Single-item list with one appended item.
        ([1, 3, 5], (2, 4, 6), [6, 4, 2, 1, 3, 5])      # 10: Appending to an odd-length list.
    ]

    all_passed = True
    sll = SinglyLinkedList()
    for i, (array, insert, expected) in enumerate(test_cases, start=1):
        try:
            sll.generate_list_from_array(array)

            for num in insert:
                sll.insert_at_beginning(num)

            result = sll.to_array()

            if result != expected:
                all_passed = False
                print(f"❌ Test {i} Failed | Input: {array}, {insert} | Expected: {expected}, Got: {result}")
        except Exception as e:
            if isinstance(expected, type) and issubclass(expected, Exception):
                if isinstance(e, expected):
                    continue
                else:
                    all_passed = False
                    print(f"❌ Test {i} Failed | Input: {array}, {insert} | Expected Exception: {expected}, Got Exception: {type(e).__name__} - {e}")
            else:
                all_passed = False
                print(f"\n⚠️ Error in test {i} | Input: {array}, {insert}")
                print(f"Exception: {e}")

    if all_passed:
        print("✅ All tests passed.")