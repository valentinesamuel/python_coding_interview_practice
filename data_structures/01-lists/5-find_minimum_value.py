def find_minimum(arr: list) -> int:
    """
    PROBLEM:Implement a function findMinimum(lst) which finds the smallest number in the given list.

    Input: A list of integers

    Output: The smallest number in the list

    Example Input: 
    arr = [9,2,3,6]

    Example Output:
    2

    APPROACH:
    - Initial thoughts: This problem can be solved by keep track of the current smallest number.

    - Plan: 
        - Iterate through the array
        - On every iteration, check if the number is smaller than the current smallest number.
        - If it is, then let the number be the current smallest number
    """

    if len(arr) == 0:
        return arr
    if arr == None:
        return
    if not isinstance(arr, list):
        raise TypeError('Invalid data type. Please input a list')

    curr_min = arr[0]
    for num in arr:
        if num < curr_min:
            curr_min = num

    return curr_min


def test_find_minimum():
    # Testcase 1: Normal input
    lst = [100, 12, 34, 40]
    expected = 12
    assert find_minimum(lst) == expected

    # Testcase 2: Empty list
    lst = []
    expected = []
    assert find_minimum(lst) == expected

    # Testcase 3: Negative values
    lst = [-2, -5, 234, -459]
    expected = -459
    assert find_minimum(lst) == expected

    print("\n\n💯💯All test cases passed!💯💯\n\n")


# Run the test cases
test_find_minimum()
