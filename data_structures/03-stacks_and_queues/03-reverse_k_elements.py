from DS_Classes.QueueClass import MyQueue as Queue
from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')


def reverseK(queue: Queue, k: int):
    """
    PROBLEM: Implement the function reverseK(queue, k) which takes a queue and a number “k” as input and reverses the first “k” elements of the queue. An illustration is also provided for your understanding. In case the value of “k” is larger than the size of the queue, is smaller than 0, or if the queue is empty, simply return None instead.

    Input: 

    Output: The queue with first “k” elements reversed. Remember to return the queue itself!

    Example Input: 
    Queue = [1,2,3,4,5,6,7,8,9,10], k = 5

    Example Output:
    Queue = [5,4,3,2,1,6,7,8,9,10]

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

    for _ in range(k):
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    for i in range(stack.size() - k):
        queue.enqueue(queue.dequeue())

    return queue
