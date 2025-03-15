from my_code.overviews._3_1_stack import Stack
from my_code.overviews._4_1_queue import Queue
from my_code._4_queue_problems.queue_dynamic_test_function import run_queue_tests

# Test creation of a queue using two stacks
def two_stack_queue(inputs):
    """Given a list of basic stack commands, enqueue, dequeue, and peek, use two stacks
       to emeulate the expected functionality of a queue
    """
    
    s1, s2 = [], []
    for query_extracted in inputs:
        print(query_extracted)
        if query_extracted[0] == 1: # Enqueue
            if s1:
                while s1:
                    s2.append(s1.pop())
                    s2.append(query_extracted[1])
            else:
                s1.append(query_extracted[1])
                while s2:
                    s1.append(s2.pop())


        elif query_extracted[0] == 2: # Dequeue
            if s1:
                while s1:
                    s2.append(s1.pop())
                    s2.pop()
            else:
                s2.pop()
        else: # peek
            if s1:
                while s1:
                    s2.append(s1.pop())
                print(s2[-1])
            else:
                print(s2[-1])


if __name__ == "__main__":

        test_cases = [
            ("abcabcbb", 3), #  1
            ("zxyzxyz", 3),  #  2
            ("xxxx", 1),     #  3
            ("aabbcc", 2),   #  4
            ("abcabcbb", 3), #  5
            ("au", 2),       #  6
            ("aab", 2),      #  7
        ]

        all_passed = True
        for idx, (string, expected) in enumerate(test_cases, start=1):
                result = two_stack_queue(string)
                if result != expected:
                    all_passed = False
                    print(result, expected, f"Test case {idx}: string={string}, expected={expected}, result {result}")
        if all_passed:
            print("No failures detected.")