def find_second_maximum(lst):
    """
    PROBLEM: Implement a function find_second_maximum(lst) which returns the second largest element in the list.

    Input: A List

    Output: Second largest element in the list

    Example Input: 
    [9,2,3,6]

    Example Output:
    6

    APPROACH:
    - Initial thoughts: Find a way to make sure that there is there is max value and the second max value will always be larger than the max value.

    - Plan: 
        - Set a max and second_max value to be a negative infinity value.
        - For every num in the list. If the num is greater than the max value, that means the current max value is going the be the new second_max value since a new max value has been found.
        - Else if the current value if greater than the second_max value, then the number becomes the current second_max value.
        - We could also check for when all the numbers in the list are the same number. This would mean that the max value never gets updated more than once and that the second_max value is still going to be a negatively infinite value because if it is all 6 then 6 cannot be greater than 6
    """

    if len(lst) <= 1:
        return float('-inf')
    if lst == None:
        return 
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')
    
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

def test_find_second_maximum():
    # Testcase 1: Normal input
    lst = [1, 2, 3, 4]
    expected = 3
    assert find_second_maximum(lst) == expected

    # Testcase 2: List with negative numbers
    lst = [-10, -5, -2, -7, -1]
    expected = -2
    assert find_second_maximum(lst) == expected

    # Testcase 3: List with duplicates
    lst = [5, 5, 3, 2, 5, 2]
    expected = 3
    assert find_second_maximum(lst) == expected

    # Testcase 4: List with single element
    lst = [10]
    expected = float('-inf')  # No second maximum exists
    assert find_second_maximum(lst) == expected

    # Testcase 5: List with repeated maximum values
    lst = [6, 6, 6, 6]
    expected = float('-inf')
    assert find_second_maximum(lst) == expected

    # Testcase 6: Empty list
    lst = []
    expected = float('-inf')  # No second maximum exists
    assert find_second_maximum(lst) == expected

    print("\n\n💯💯All test cases passed!💯💯\n\n")

# Run the test cases
test_find_second_maximum()