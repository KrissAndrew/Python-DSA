import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def run_stack_tests(stack, func, test_cases, result_extractor=None):
    """
    Generalized test runner for stacks.
    """
    all_passed = True
    for i, (input_data, expected) in enumerate(test_cases, start=1):
        try:
            # ✅ Only initialize the list if `stack` is not None
            if stack is not None:
                stack.generate_stack_from_array(input_data if isinstance(input_data, list) else input_data[0])

            # ✅ Call function if provided and `stack` is not None
            if func and stack is not None:
                getattr(stack, func.__name__)()

            # ✅ Ensure extractor is called correctly
            if result_extractor:
                result = result_extractor(stack, input_data) if stack is not None else result_extractor(input_data)

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
