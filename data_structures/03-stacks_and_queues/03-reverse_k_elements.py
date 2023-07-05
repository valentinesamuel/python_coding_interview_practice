from QueueClass import MyQueue
from StackClass import MyStack as Stack

def reverseK(queue, k):
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