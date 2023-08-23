def binary_search(lst, n):
    left = 0
    right = len(lst) - 1
    found = False

    while left <= right and not found:
        mid = (left + right) // 2
        if lst[mid] == n:
            found = True
        else:
            if lst[mid] > n:
                right = mid - 1
            if lst[mid] < n:
                left = mid + 1
    return found


def pivoted_binary_search(lst, target):
    l = 0
    r = len(lst)-1

    while l <= r:
        mid = (l+r) // 2
        if target == lst[mid]:
            return mid

        # left sorted part of the input array
        if lst[l] <= lst[mid]:
            # if the target is between the left most and
            # mid position of the left part of the input array
            if target < lst[mid] and target >= lst[l]:
                r = mid - 1
            else:
                l = mid + 1
        # right sorted part of the input array
        else:
            # if the target is between the right most and
            # mid position of the right part of the input array
            if target > lst[mid] and target <= lst[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


nums = [8, 11, 13, 15, 1, 4, 6]
target = 1
index = pivoted_binary_search(nums, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print("Element not found.")
