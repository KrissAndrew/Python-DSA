# Test and implement a linked lists display/print functionality
# For the sake of this I will implement a __str__(self) function in my linked list classes
import io
import sys
from overviews._2_0_singly_linked_list import SinglyLinkedList

def test_display_list(sll: SinglyLinkedList):
    # Capture the output
    captured_output = io.StringIO()
    sys.stdout = captured_output  # Redirect stdout
    print(sll)           # This will print to captured_output
    sys.stdout = sys.__stdout__  # Reset stdout back to normal    
    return captured_output.getvalue().strip()

if __name__ == "__main__":
    
    test_cases = [
        ([], Exception),                           #  1
        ([1], "1 -> None"),                        #  2
        ([1, 2, 3], "1 -> 2 -> 3 -> None"),        #  3
        ([1, 2, 3, 4], "1 -> 2 -> 3 -> 4 -> None") #  4
    ]

    all_passed = True
    sll = SinglyLinkedList()
    for i, (inputs, expected) in enumerate(test_cases, start=1):
        try:
            # If inputs is a tuple, unpack it; otherwise, pass it as a single argument
            sll.generate_list_from_array(*inputs) if isinstance(inputs, tuple) else sll.generate_list_from_array(inputs)

            result = test_display_list(sll)

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