def rearrange(lst):
    leftMostIndex = 0
    for idx in range(len(lst)):
        if lst[idx] < 0:
            if idx != leftMostIndex:
                lst[idx], lst[leftMostIndex] = lst[leftMostIndex], lst[idx]
            leftMostIndex += 1
    return lst


