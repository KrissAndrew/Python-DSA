import sys
import os
from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList  # Ensure you import correctly

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def run_sll_tests(sll, func, test_cases, result_extractor=None):
    """
    Generalized test runner for singly linked lists.
    """
    all_passed = True

    for i, (input_data, expected) in enumerate(test_cases, start=1):
        try:
            # ✅ Only initialize the list if `sll` is not None
            if sll is not None:
                sll.generate_list_from_array(input_data if isinstance(input_data, list) else input_data[0])

            # ✅ Call function if provided and `sll` is not None
            if func and sll is not None:
                getattr(sll, func.__name__)()

            # ✅ Ensure extractor is called correctly
            if result_extractor:
                result = result_extractor(sll, input_data) if sll is not None else result_extractor(input_data)

                # ✅ Compare node data if we are expecting a Node
                if isinstance(expected, SinglyLinkedList.Node) and isinstance(result, SinglyLinkedList.Node):
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
