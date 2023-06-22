def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        # to make sure that k is within the bounds of the list
        k = k % len(lst)
    rotated_list = lst[::-1]
    left = rotated_list[:k][::-1]
    right = rotated_list[k:][::-1]

    return left+right


print(right_rotate(['right', 'rotate', 'python'], 4))
