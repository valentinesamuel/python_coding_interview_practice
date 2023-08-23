def sort_binary_list(lst):

    j = 0

    for i in range(len(lst)):
        if lst[i] < 1:
            lst[j], lst[i] = lst[i], lst[j]
            j += 1

    return lst
