def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        if left[i] > right[j]:
            res.append(right[j])
            j += 1

    left += left[i:]
    right += right[j:]

    return res
