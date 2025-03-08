class Stack:
    
    def __init__(self):
        self.stack = []
        self.max_values = []

    def __len__(self):
        return len(self.stack)
    
    # O(1) running time
    def is_empty(self):
        return self.stack == []

    # O(1) running time
    def push(self, data):
        if self.is_empty():
            self.max_values.append(data) # If empty value will always be max

        elif data >= self.max_values[-1]:
            self.max_values.append(data)
        self.stack.append(data)

    # O(1) because we manipulate the last item
    def pop(self):

        if self.is_empty():
            return None
        
        data = self.stack[-1]
        del self.stack[-1]
        if self.max_values[-1] == data:
            del self.max_values[-1]
        return data

    # O(1) constant running time
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    # O(1) - python arrays track a length characteristic
    def size_stack(self):
        return len(self.stack)
    
    def max_value(self):
        if not self.is_empty():
            return self.max_values[-1]
        return None
    
    # O(n) - needs to assign new node items for each item in provided array
    def generate_stack_from_array(self, array: list[int]):
        for data in array:
            self.push(data)
        return True
    