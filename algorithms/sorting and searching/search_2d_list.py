def find_in(lst: list, number: int):
    rows = len(lst)
    cols = len(lst[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        midpoint = (left + right) // 2
        midpoint_element = lst[int(midpoint/cols)][int(midpoint % cols)]
        if number == midpoint_element:
            return True
        elif number > midpoint_element:
            left = midpoint + 1
        elif number < midpoint_element:
            right = midpoint - 1

    return True


def find_in2(lst: list, number: int):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left+right) // 2
        if number in lst[mid]:
            return True
        elif number > lst[mid][0] and number < lst[mid][-1]:
            return number in lst[mid]
        if number > lst[mid][-1]:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(find_in2([[10, 11, 12, 13], [14, 15, 16, 17],
      [27, 29, 30, 31], [32, 33, 39, 80]], 10))
print(find_in2([[10, 11, 12, 13], [14, 15, 16, 17],
      [27, 29, 30, 31], [32, 33, 39, 80]], 10))
print()
