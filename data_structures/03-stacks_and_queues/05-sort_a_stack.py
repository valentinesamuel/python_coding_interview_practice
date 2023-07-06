from StackClass import MyStack as Stack


def sort_stack(stack: Stack):
    temp_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack
