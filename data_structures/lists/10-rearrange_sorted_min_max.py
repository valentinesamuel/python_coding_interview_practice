def max_min(lst):

    left = 0
    right = len(lst) - 1
    res = []
    while left <= right:
        if left == right:
            res.append(lst[left])
        else:
            res.append(lst[right])
            res.append(lst[left])
        left+=1
        right-=1
    return res

