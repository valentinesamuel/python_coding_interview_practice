def rearrange(lst):
    """
    PROBLEM: Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

    Input: A list of integers

    Output: A list with negative elements at the left and positive elements at the right

    Example Input: 
    [10,-1,20,4,5,-9,-6]

    Example Output:
    [-1,-9,-6,10,20,4,5]

    APPROACH:
    - Initial thoughts: We can use a two pointers for this

    - Plan: 
        - Let the leftmostindex be 0 as it is the first item in the array
        - Iterate through the array
        - For every item, if the item is less that 0
        - Check if it item is less than 0
        - Then make sure that current index is not the same with the leftmost element so that we don't swap the same item at the same index.
        - So long as the item is less than 0, we move the leftmost index
    """

    if len(lst) == 0:
        return lst
    if lst == None:
        return
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')

    leftMostIndex = 0
    for idx in range(len(lst)):
        if not isinstance(lst[idx], int):
            return None
        if lst[idx] < 0:
            if idx != leftMostIndex:
                lst[idx], lst[leftMostIndex] = lst[leftMostIndex], lst[idx]
            leftMostIndex += 1
    return lst


def test_rearrange():
    # Testcase 1: Normal input with both negative and positive numbers
    lst = [10, -1, 20, 4, 5, -9, -6]
    expected = [-1, -9, -6, 4, 5, 10, 20]
    assert rearrange(lst) == expected

    # Testcase 2: All negative numbers
    lst = [-5, -10, -3, -2, -1]
    expected = [-5, -10, -3, -2, -1]
    assert rearrange(lst) == expected

    # Testcase 3: All positive numbers
    lst = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert rearrange(lst) == expected

    # Testcase 4: Empty list
    lst = []
    expected = []
    assert rearrange(lst) == expected

    # Testcase 5: List with zero
    lst = [0, -2, 0, 5, -1, 0]
    expected = [-2, -1, 0, 5, 0, 0]
    assert rearrange(lst) == expected

    # Testcase 6: List with mixed integers and non-integers
    lst = [1, -3, 2.5, -4, 'a', -6]
    expected = None
    assert rearrange(lst) == expected

    print("\n\n💯💯All test cases passed!💯💯\n\n")


test_rearrange()
