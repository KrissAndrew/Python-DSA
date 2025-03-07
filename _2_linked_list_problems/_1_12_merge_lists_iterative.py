# Test merging of two sorted singly linked lists using an iterative approach. 
if __name__ == "__main__":

    from overviews._2_0_singly_linked_list import SinglyLinkedList

    test_cases = [
        (([], []), []),          #  1
        (([1], [1]), [1, 1]),        #  2
        (([1, 2], [1]), [1, 1, 2]), #  3
        (([2, 1], [2, 1]), [1, 1, 2, 2]),  #  4
        (([3, 2, 1], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),  #  4
    ]

    all_passed = True
    sll1, sll2 = SinglyLinkedList(), SinglyLinkedList()
    for i, (inputs, expected) in enumerate(test_cases, start=1):
        try:
            sll1.generate_list_from_array(inputs[0])
            sll1.sort()
            sll2.generate_list_from_array(inputs[1])
            sll2.sort()
            sll1.sorted_merge_iterative(sll1.get_head_node(), sll2.get_head_node())
            result = sll1.to_array()

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