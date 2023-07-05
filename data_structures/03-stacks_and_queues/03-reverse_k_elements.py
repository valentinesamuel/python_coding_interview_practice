from QueueClass import MyQueue
from StackClass import MyStack as Stack

def reverseK(queue, k):
    """
    PROBLEM: 

    Input: 

    Output: 

    Example Input: 
    n = 3

    Example Output:
    result = ["1","10","11"]

    APPROACH:
    - Initial thoughts: I tried but i could not solve it before my trial time of 30 mins elapsed

    - Plan: 
        - using an auxiliary stack, remove the first k elements from the queue and add it to the stack
        - enqueue all the elements by popping them from the stack
        - starting from  queue_length - k, dequeue all elements and enqueue them
    """
    if k > queue.size() or k < 0 or queue.is_empty():
        return None

    stack = Stack()

    for i in range(k):
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    for i in range(stack.size() - k):
        queue.enqueue(queue.dequeue())
    
    return queue