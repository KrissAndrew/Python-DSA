import io
import sys
from my_code.overviews._2_0_singly_linked_list import SinglyLinkedList
from my_code._2_0_linked_list_problems.sll_dynamic_test_function import sll_run_tests

# Test and implement singly linked list classes print functionality

def test_display_list(sll: SinglyLinkedList, _):
    # Ensure it raises an exception when the list is empty
    if sll.head is None:
        raise Exception("Cannot display an empty list.")

    # Capture the output
    captured_output = io.StringIO()
    sys.stdout = captured_output  # Redirect stdout
    print(sll)  # Print to captured_output
    sys.stdout = sys.__stdout__  # Reset stdout to normal    
    return captured_output.getvalue().strip()


if __name__ == "__main__":
    
    test_cases = [
        ([], Exception),                           #  1
        ([1], "1 → None"),                        #  2
        ([1, 2, 3], "1 → 2 → 3 → None"),        #  3
        ([1, 2, 3, 4], "1 → 2 → 3 → 4 → None") #  4
    ]

    sll = SinglyLinkedList()
    sll_run_tests(sll, None, test_cases, test_display_list)
