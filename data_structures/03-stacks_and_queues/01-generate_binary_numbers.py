from QueueClass import MyQueue


def find_bin(number):
    """
    PROBLEM: Implement a function find_bin(n) which will generate binary numbers from 1 till n in the form of a string using a queue. The MyQueue and MyStack classes are provided in all of these challenges. An illustration is also provided for your understanding.

    Input: A positive integer n

    Output: Returns binary numbers in the form of strings from 1 up to n

    Example Input: 
    n = 3

    Example Output:
    result = ["1","10","11"]

    APPROACH:
    - Initial thoughts: I tried but i could not solve it before my trial time of 30 mins elapsed

    - Plan: 
        - create a queue and enqueue 1
        - until n,
            - dequeue the queue, stringify the value and append it to the result list
            - enqueue two variations of the dequeue value, one that ends with 0 and another one that ends with 1
    """
        
    if not isinstance(number, int):
        return

    res = []
    queue = MyQueue()
    queue.enqueue(1)

    for i in range(number):
        res.append(str(queue.dequeue()))
        s1 = res[i] + "0"
        s2 = res[i] + "1"

        queue.enqueue(s1)
        queue.enqueue(s2)

    return res
