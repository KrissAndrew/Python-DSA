from my_code.overviews._4_1_queue import Queue
from my_code._4_queue_problems.queue_dynamic_test_function import run_queue_tests

# Test returning the max value in a stack

if __name__ == "__main__":


    test_cases = [
        ([], None),           #  1: Delete from empty list.
        ([1], 1),             #  2: Inserting into an empty list, invalid position
        ([1, 2], 2),          #  3: Delete multiple items.
        ([1, 2, 3], 3),       #  4: Delete central item multiple items into a non-empty list.
        ([9, 1, 1, 1, 9], 9), #  5: Delete multiple of same item.
    ]

    queue = Queue()
    run_queue_tests(queue, queue.pop(), test_cases)