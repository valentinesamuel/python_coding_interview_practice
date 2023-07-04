class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size
        self.top1 = -1
        self.top2 = self.size

    def __repr__(self) -> str:
        return str(self.arr)

    def push1(self, value):
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print('Overflow')
            exit(1)

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2-1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print('Stack overflow')
            exit(1)

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        else:
            print('Stack overflow')
            exit(1)

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.t2 <= self.size-1:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print('Stack overflow')
            exit(1)

twostck = TwoStacks(6)
twostck.push1(2)
twostck.push1(0)
twostck.push2(5)
twostck.push2(2)
twostck.push2(7)
twostck.push2(1)
twostck.pop1()
twostck.pop1()
twostck.pop2()
print(twostck)