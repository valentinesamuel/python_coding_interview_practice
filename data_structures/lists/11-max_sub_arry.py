def find_max_sum_sublist(lst):
    """
    PROBLEM: Given an unsorted list A, the maximum sum sub list is the sub list (contiguous elements) from A for which the sum of the elements is maximum. In this challenge, we want to find the sum of the maximum sum sub list. This problem is a tricky one because the list might have negative integers in any position, so we have to cater to those negative integers while choosing the continuous sublist with the largest positive values.

    Input: A list with random integers.

    Output: A number (maximum subarray sum)

    Example Input: 
    my_list = [-4, 2, -5, 1, 2, 3, 6, -5, 1]  

    Example Output:
    my_list = 12

    APPROACH:
    - Initial thoughts: I did not really know what to do at first. So I looked up some  explanations. 

    - Plan: 
        - Keep track of the max sum and the current sum
        - Iterate through the array
        - Calculate the current sum by either adding the current element to the previous sum or starting an new sublist if the current element is greater than the previous sum
        - The max sum is updated is the current sum becomes larger.
    """

    if lst == None:
        return
    if len(lst) == 0:  # Empty list case
        return 0
    if not isinstance(lst, list):
        raise Exception('Invalid data type. Please input a list')
    
    max_sum = lst[0]
    curr_sum = lst[0]
    for idx in range(1, len(lst)):
        curr_sum = max(lst[idx], curr_sum + lst[idx])
        max_sum = max(curr_sum, max_sum)
    return max_sum


def test_find_max_sum_sublist():
    # Testcase 1: Normal input with positive and negative numbers
    lst1 = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    assert find_max_sum_sublist(lst1) == 9

    # Testcase 2: Normal input with all negative numbers
    lst2 = [-2, -3, -4, -1, -2, -1, -5]
    assert find_max_sum_sublist(lst2) == -1

    # Testcase 3: Normal input with all positive numbers
    lst3 = [1, 2, 3, 4, 5]
    assert find_max_sum_sublist(lst3) == 15

    # Testcase 4: Empty list
    lst4 = []
    assert find_max_sum_sublist(lst4) == 0

    # Testcase 5: List with a single element
    lst5 = [5]
    assert find_max_sum_sublist(lst5) == 5

    # Testcase 6: List with None as input
    lst6 = None
    assert find_max_sum_sublist(lst6) is None

    # Testcase 7: Invalid data type input (not a list)
    lst7 = "invalid"
    try:
        find_max_sum_sublist(lst7)
    except Exception as e:
        assert str(e) == 'Invalid data type. Please input a list'

    print("\n\n💯💯All test cases passed!💯💯\n\n")


test_find_max_sum_sublist()
