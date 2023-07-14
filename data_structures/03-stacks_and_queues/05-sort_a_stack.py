from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')


def sort_stack(stack: Stack):
    """
    PROBLEM: Implement a function called sort_stack() which takes a stack and sorts all of its elements in ascending order such that when they are popped and printed, they come out in ascending order. So the element that was pushed last to the stack has to be the smallest.

    Input: A stack of integers.

    Output: The stack with all its elements sorted in descending order.

    Example Input: 
    stack = [23, 60, 12, 42, 4, 97, 2]

    Example Output:
    result = [97, 60, 42, 23, 12, 4, 2]
    2 was the value last pushed

    APPROACH:
    - Initial thoughts: I tried but i could not solve it before my trial time of 30 mins elapsed

    - Plan: 
        - create a temporary stack
        - untill the main stack is empty
        - pop an item from the main stack
        - while the temporary stacy is not empty and the last item on the temporary stack is greater than then item that was popped from the main stack
        - pop items from the temporary stack and push them to the main stack
        - but if the above 2 conditions are false, push the popped item to the temporaray stack
        - this should result in a backwardly ordered stack (descending order).
        - then pop all the elements from the temp stack to the main stack
    """
    temp_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack
