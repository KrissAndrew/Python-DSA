import sys
import os
from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList

# Get the absolute path of the 'code/' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def sll_run_tests(sll, func, test_cases, result_extractor=None):
    """
    Generalized test runner for singly linked lists.
    """
    all_passed = True

    for i, (input_data, expected) in enumerate(test_cases, start=1):
        try:
            sll.generate_list_from_array(input_data if isinstance(input_data, list) else input_data[0])

            # ✅ If func exists, call it
            if func:
                getattr(sll, func.__name__)()

            # ✅ Ensure extractor is called with correct inputs
            if result_extractor:
                result = result_extractor(sll, input_data)

                # ✅ Compare node data if we are expecting a Node
                if isinstance(expected, sll.Node) and isinstance(result, sll.Node):
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

