from StackClass import MyStack as Stack


def is_balanced(exp):
    closing = ['}', ')', ']']
    stack = Stack()
    for character in exp:
        if character in closing:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if character == '}' and top_element != '{':
                return False
            if character == ')' and top_element != '(':
                return False
            if character == ']' and top_element != '[':
                return False
        else:
            stack.push(character)
    if not stack.is_empty():
        return False
    return True

