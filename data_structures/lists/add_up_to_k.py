def find_sum(lst, k):
    register = {}
    res = []
    for num in lst:
        key = k - num
        if key not in register:
            register[num] = key
        else:
            res.append(key)
            res.append(num)
    return res



print(find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81))
