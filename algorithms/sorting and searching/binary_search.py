def binary_search(lst, n):
    left = 0
    right = len(lst) - 1
    found = False

    while left <= right and not found:
        mid =  (left + right) // 2
        if lst[mid] == n:
            found = True
        else:
            if lst[mid] > n:
                right = mid - 1
            if lst[mid] < n:
                left = mid + 1
    return found
