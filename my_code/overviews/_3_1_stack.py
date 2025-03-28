class Stack:
    
    def __init__(self):
        self.stack = []
        self.total = 0
        self.max_values = []

    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        if len(self) == 0:
            return "Empty list"  # Instead of raising an exception
        return str(self.stack)
        
    def __reversed__(self):
        reversed_stack = Stack()
        reversed_stack.stack = list(reversed(self.stack))
        reversed_stack.max_values = list(reversed(self.max_values))
        return reversed_stack

    # O(1) running time
    def is_empty(self):
        return not self.stack

    # O(1) running time
    def push(self, data):
        if self.is_empty() or data >= self.max_values[-1]:
            self.max_values.append(data)
        self.stack.append(data)
        self.total += data

    # O(1) because we manipulate the last item
    def pop(self):

        if self.is_empty():
            return None
        
        data = self.stack[-1]
        del self.stack[-1]
        if self.max_values[-1] == data:
            del self.max_values[-1]
        self.total -= data
        return data

    # O(1) constant running time
    def peek(self):
        return self.stack[-1] if self.stack else None

    # O(1) - python arrays track a length characteristic
    def size_stack(self):
        return len(self.stack)
    
    def max_value(self):
        return self.max_values[-1] if self.max_values else None

    # O(n) - needs to assign new node items for each item in provided array
    def generate_stack_from_array(self, array: list[int]):
        if not array:
            return self  # Return self for method chaining
        for data in array:
            self.push(data)
        return self
    
    def reverse_stack(self):
        # Reverse the main stack
        self.stack.reverse()
        
        # Rebuild max_values from the reversed stack
        self.max_values = []
        current_max = float('-inf')
        for value in self.stack:
            if value >= current_max:
                self.max_values.append(value)
                current_max = value

    
if __name__ == "__main__":
    s1 = Stack().generate_stack_from_array([3, 2, 1, 1, 1])
    s2 = Stack().generate_stack_from_array([4, 3, 2])
    s3 = Stack().generate_stack_from_array([1, 1, 4, 1])

    s1.reverse_stack()
    s2.reverse_stack()
    s3.reverse_stack()

    print(s1)
    print(s2)
    print(s3)
