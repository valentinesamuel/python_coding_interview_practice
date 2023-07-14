class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()


class MinStack:
    def __init__(self):
        self.main_stack = MyStack()
        self.min_stack = MyStack()
    
    def pop(self):
        self.main_stack.pop()
        return self.min_stack.pop()

    def push(self, value):
        self.main_stack.push(value)
        # if the stack is empty or the value we are bringing is smaller than the current smaller item at the top of the stack
        if self.min_stack.is_empty() or value < self.min_stack.peek():
            self.min_stack.push(value)
        else:
            # we are still pushing the last item on the stack even if the smallest number remains the same so that we can have equal number of items in both stacks at every given time
            self.min_stack.push(self.min_stack.peek())
        
    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        return None