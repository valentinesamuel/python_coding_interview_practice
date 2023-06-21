def find_second_maximum(lst):

    
    max = float('-inf')
    second_max = float('-inf')
    for num in lst:
        if num > max:
            second_max = max
            max = num
        elif num > second_max and num < max:
            second_max = num

    # Check if all the values in the list are the same
    if second_max == float('-inf'):
        return float('-inf')
    
    return second_max

