class TwoStacks:
    """
    PROBLEM: Implement the following functions to implement two stacks using a single array such that for storing elements both stacks should use the same array. An illustration is also provided for your understanding. Also, for this problem, initialize a Python list with the provided fixed size and perform all the operations in-place without growing or shrinking the list!

    Input/Output
    push1(value)
    Input: an integer
    Output: inserts the given value in the first stack, i.e., stack1

    push2(value)
    Input: an integer
    Output: inserts the given value in the second stack i.e stack2

    pop1()
    Output: returns and removes the top value of stack1

    pop2()
    Output: returns and removes the top value of stack2


    APPROACH:
    - Initial thoughts: I tried but i could not solve it before my trial time of 30 mins elapsed

    Plan: Check the methods
    """
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size
        self.top1 = -1
        self.top2 = self.size

        """
        We are backing the stacks against each other. i.e, the top of every stack starts at the opposite end of the list. This will make them to be able to push or pop values based on the number of available spaces in the whole array 
        """
    def __repr__(self) -> str:
        return str(self.arr)

    def push1(self, value):
        """
        - first check that there us at least one empty space in the stack for us to push to
        - we do this by checking that the top of the left stack is less than the top of the right stack
        - if true, we then move the top of the stack one step forward(to the right of the list means adding 1) and insert the element at the index of the stacks's top pointer
        - if false, we return
        """
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print('Overflow')
            exit(1)

    # Insert Value in Second Stack
    def push2(self, value):
        """
        - first check that there us at least one empty space in the stack for us to push to
        - we do this by checking that the top of the left stack is less than the top of the right stack
        - if true, we then move the top of the stack one step backward(to the left of the list means subtracting 1) and insert the element at the index of the stacks's top pointer
        - if false, we return
        """
        if self.top1 < self.top2-1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print('Stack overflow')
            exit(1)

    # Return and remove top Value from First Stack
    def pop1(self):
        """
        - we check if there is an element to pop by checking if the stack's top pointer is at 0 or it has moved forward
            - since it at -1 by default, if it goes to 0, that means, there has been an insert
        - if true, then we get the element in the index of the stack's top pointer, save it and replace that element with None and return the saved value
        """
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        else:
            print('Stack overflow')
            exit(1)

    def pop2(self):
        """
        - we check if there is an element to pop by checking if the stack's top pointer is at the default position
            - since it at the end of the array by default, if it becomes less than the array's length, that means, there has been an insert
        - if true, then we get the element in the index of the stack's top pointer, save it and replace that element with None and return the saved value
        """
        if self.t2 <= self.size-1:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print('Stack overflow')
            exit(1)

