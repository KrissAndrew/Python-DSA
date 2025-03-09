import sys
import os
from my_code.overviews._2_1_doubly_linked_list import DoublyLinkedList

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def run_sll_tests(dll, func, test_cases, result_extractor=None):
    """
    Generalized test runner for singly linked lists.
    """
    all_passed = True

    for i, (input_data, expected) in enumerate(test_cases, start=1):
        try:
            # ✅ Only initialize the list if `dll` is not None
            if dll is not None:
                dll.generate_list_from_array(input_data if isinstance(input_data, list) else input_data[0])

            # ✅ Call function if provided and `dll` is not None
            if func and dll is not None:
                getattr(dll, func.__name__)()

            # ✅ Ensure extractor is called correctly
            if result_extractor:
                result = result_extractor(dll, input_data) if dll is not None else result_extractor(input_data)

                # ✅ Compare node data if we are expecting a Node
                if isinstance(expected, DoublyLinkedList.Node) and isinstance(result, DoublyLinkedList.Node):
                    if result.data != expected.data:  # Compare `.data` of nodes
                        all_passed = False
                        print(f"❌ Test {i} Failed | Input: {input_data} | Expected Node Data: {expected.data}, Got: {result.data}")

                # ✅ Otherwise, do normal comparison
                elif result != expected:
                    all_passed = False
                    print(f"❌ Test {i} Failed | Input: {input_data} | Expected: {expected}, Got: {result}")

        except Exception as e:
            if expected == Exception:
                continue  # Expected exception raised, test passes
            else:
                all_passed = False
                print(f"❌ Test {i} Failed | Unexpected Exception: {type(e).__name__} - {e}")

    if all_passed:
        print("✅ All tests passed.")
