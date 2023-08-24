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
