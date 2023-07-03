from QueueClass import MyQueue


def find_bin(number):
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
