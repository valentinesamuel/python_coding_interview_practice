from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')


class NewQueue:
    """
    PROBLEM: You have to implement the enqueue() and dequeue() functions using the MyStack class we created earlier. enqueue( ) will insert a value into the queue and dequeue( ) will remove a value from the queue.

    Input
    enqueue( ): A value to insert into the queue
    dequeue( ): Does not require any input

    Output
    enqueue( ): Does not return anything
    dequeue( ): Pops out and returns the oldest value in   the queue

    Example Input: 
    value = 5 # [1, 2, 3, 4]
    enqueue(value)
    dequeue()

    Example Output:
    True # [1, 2, 3, 4, 5]
    1 # [2, 3, 4, 5]

    APPROACH:
    - Initial thoughts: Maybe i could use another reversed version of the main stack

    - Plan: 
        - to enqueue, just push on the main stack
        - to dequeue, we can reverse the mainstack anytime we want to dequeue and pop it
        - to reverse, we pop of the main stack and push it on the temporary stack
    """

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
