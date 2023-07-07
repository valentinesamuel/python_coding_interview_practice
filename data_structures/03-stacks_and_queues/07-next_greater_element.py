from StackClass import MyStack as Stack


def next_greater_element(lst):
    stack = Stack()
    res = [-1] * len(lst)

    for i in range(len(lst)):
        if not stack.is_empty():
            while not stack.is_empty() and stack.peek <= lst[i]:
                stack.pop()

        if not stack.is_empty():
            res[i] = stack.peek

        stack.push(lst[i])

    return res
