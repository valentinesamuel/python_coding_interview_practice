def find_max_sum_sublist(lst):
    if not lst:  # Empty list case
        return 0
    max_sum = lst[0]
    curr_sum = lst[0]
    for idx in range(1, len(lst)):
        curr_sum = max(lst[idx], curr_sum + lst[idx])
        max_sum = max(curr_sum, max_sum)
    return max_sum
