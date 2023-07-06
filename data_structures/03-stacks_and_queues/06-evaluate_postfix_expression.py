from StackClass import MyStack as Stack


def evaluate_post_fix(exp: str):
    stack = Stack
    for ele in exp:
        if ele.isdigit():
            stack.push(ele)
        else:
            left = stack.pop()
            right = stack.pop()
            stack.push(str(eval(right + ele + left)))
    return int(float(stack.pop()))
