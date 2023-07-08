from StackClass import MyStack as Stack


def next_greater_element(lst):
    """
    PROBLEM: You are required to implement the next_greater_element() function. For each element "i" in a list, the function finds the first element to its right which is greater than element i. If for any element such a value does not exist, the answer is -1.
    Note: The next greater element is the first element towards the right which is greater than the given element. For example, in the list [1, 3, 8, 4, 10, 5], the next greater element of 3 is 8 and the next greater element for 8 is 10.

    Input: An integer list.

    Output: A list containing the next greater element of each element from the input list.

    Example Input: 
    list = [4, 6, 3, 2, 8, 1]

    Example Output:
    result = [6, 8, 8, 8, -1, -1]

    APPROACH:
    - Initial thoughts: I tried but the solution i had was in quadratic time and it had a bug where the last element was not getting processed

    - Plan: 
        - create a result array and a stack
        - for every element in the list, if the stack is not empty
            - while the stack is not empty and the first item on the list is less than or equal to the current element, pop the stack 
        - if the stack is empty, insert -1 at the index of the current element in the result list else, add the first value(peek) in the stack to the current index in the result array
        - finally, push the current element to the stack
    """

    stack = Stack()
    res = [-1] * len(lst)

    for i in range(len(lst)):
        if not stack.is_empty():
            while not stack.is_empty() and stack.peek <= lst[i]:
                stack.pop()

        if not stack.is_empty():
            res[i] = stack.peek()

        stack.push(lst[i])

    # we are basically using the stack to store elements whose next greater element have not been found

    return res
