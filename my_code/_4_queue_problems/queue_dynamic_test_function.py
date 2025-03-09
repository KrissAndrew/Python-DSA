import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def run_queue_tests(queue, func, test_cases, result_extractor=None):
    """
    Generalized test runner for stacks.
    """
    all_passed = True
    for i, (input_data, expected) in enumerate(test_cases, start=1):
        try:
            # ✅ Only initialize the list if `queue` is not None
            if queue is not None:
                queue.generate_queue_from_array(input_data if isinstance(input_data, list) else input_data[0])

            # ✅ Call function if provided and `queue` is not None
            if func and queue is not None:
                getattr(queue, func.__name__)()

            # ✅ Ensure extractor is called correctly
            if result_extractor:
                result = result_extractor(queue, input_data) if queue is not None else result_extractor(input_data)

                # ✅ Compare results to expected
                if result != expected:
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
