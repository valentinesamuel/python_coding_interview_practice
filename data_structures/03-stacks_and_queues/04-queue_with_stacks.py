from StackClass import MyStack as Stack


class NewQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    def enqueue(self, value):
        self.main_stack.push(value)

    def dequeue(self):
        self.reverse()
        return self.temp_stack.pop()

    def reverse(self):
        while not self.main_stack.is_empty():
            self.temp_stack.push(self.main_stack.pop())
