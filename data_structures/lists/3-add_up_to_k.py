def find_sum(lst, k):
    """
    PROBLEM: Given a list and a number "k", find two numbers from the list that sum to "k".

    Input: A list and a number k

    Output: A list with two integers a and b that add up to k

    Example Input: 
    lst = [1,21,3,14,5,60,7,6]
    k = 81

    Example Output:
    lst = [21,60]

    APPROACH:
    - Initial thoughts: This problem can be solved using a python dictionary.

    - Plan: 
        - Iterate through the array
        - On every iteration, check if the number exists in the python dictionary.
        - If it does, return the number from the dictionary and its payload.
        - If it does not, store number as the key as the key and the remainder(target_total - number) in the dictionary. i.e { list_number : remainder }
        - Because it is easier to check if the remainant exists in the dictionary than to check for the actual number. i.e we only check if the remainant has appeared in the list by using the list_number as key.
    """

    if len(lst) == 0:
        return lst
    if lst == None:
        return 
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')
    if not isinstance(k, int):
        raise TypeError('Invalid data type. Please input a number')

    register = {}
    res = []
    for num in lst:
        payload = k - num
        if payload not in register:
            register[num] = payload
        else:
            res.append(payload)
            res.append(num)
    return res

def test_find_sum():
    # Testcase 1: Normal input
    lst, k = [1, 21, 3, 14, 5, 60, 7, 6], 81
    expected = [21, 60]
    assert find_sum(lst, k) == expected

    # Testcase 2: No solution
    lst, k = [1, 2, 3, 4, 5], 10
    expected = []
    assert find_sum(lst, k) == expected

    # Testcase 3: Empty list
    lst, k = [], 5
    expected = []
    assert find_sum(lst, k) == expected


    print("\n\n💯💯All test cases passed!💯💯\n\n")
    
# Run the test cases
test_find_sum()