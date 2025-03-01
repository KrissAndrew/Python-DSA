def run_tests(func, test_cases):
    """
    Runs test cases on the provided function and prints results.
    
    :param func: Function to be tested.
    :param test_cases: List of tuples (input(s), expected_output).
    """
    all_passed = True
    for i, (inputs, expected) in enumerate(test_cases, start=1):
        try:
            # If inputs is a tuple, unpack it; otherwise, pass it as a single argument
            result = func(*inputs) if isinstance(inputs, tuple) else func(inputs)

            if result != expected:
                all_passed = False
                print(f"❌ Test {i} Failed | Input: {inputs} | Expected: {expected}, Got: {result}")
        except Exception as e:
            all_passed = False
            print(f"\n⚠️ Error in test {i} | Input: {inputs}")
            print(f"Exception: {e}")

    if all_passed:
        print("✅ All tests passed successfully.")
