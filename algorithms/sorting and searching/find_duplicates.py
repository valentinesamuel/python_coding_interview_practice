def find_duplicates(lst):
    result = []

    for i in range(len(lst)):
        if lst[abs(lst[i])] > 0:
            lst[abs(lst[i])] = -lst[abs(lst[i])]
        else:
            result.apend(lst[abs(lst[i])])
    result = list(dict.fromkeys(result))
    return result
