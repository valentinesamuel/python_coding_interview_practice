def quick_sort(arr, left, right):
    if left < right:
        partition_idx = partition(arr, left, right)
        left = partition(arr, left, partition_idx-1)
        right = partition(arr, partition_idx+1, right)

    return arr


def partition(arr, left, right):
    partition_at = arr[right]
    pivot = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[partition_at], arr[j] = arr[j], arr[partition_at]
            partition_at += 1

    arr[partition_at], arr[right] = arr[right], arr[partition_at]
    return partition_at
