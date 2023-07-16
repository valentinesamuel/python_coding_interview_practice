def find_first_unique(lst: list) -> int:
    """
    PROBLEM: Implement a function, find_first_unique(lst) that returns the first unique integer in the list.

    Input: A list of integers

    Output: The first unique element in the list

    Example Input: 
    [9,2,3,2,6,6]

    Example Output:
    9

    APPROACH:
    - Initial thoughts: We can use a hashmap for this problem by keeping track of their frequencies.

    - Plan: 
        - Iterate through the array
        - For every item, check if the item exists in the hashmap
        - If it does, get the value and add 1 to it
        - If it does not, add the number and give it a frquency of 0
        - Iterate through the keys of the dictionary
        - if the value of that key is one, then that is the first value or number that occured once.
    """

    if len(lst) == 0:
        return None
    if lst == None:
        return
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')

    register = {}
    for num in lst:
        if num not in register:
            register[num] = 1
        else:
            value = register.get(num, 1)
            register[num] = value+1
    for key in register.keys():
        if register[key] == 1:
            return key


def test_find_first_unique():
    # Testcase 1: Normal input
    lst = [1, 2, 3, 4]
    expected = 1
    assert find_first_unique(lst) == expected

    # Testcase 2: Empty list
    lst = []
    expected = None
    assert find_first_unique(lst) == expected

    # Testcase 3: List with one element
    lst = [5]
    expected = 5
    assert find_first_unique(lst) == expected

    # Testcase 4: List with zeros
    lst = [0, 2, 9, 0, 12, 25]
    expected = 2
    assert find_first_unique(lst) == expected

    # Testcase 5: List with negative numbers
    lst = [-1, 2, -3, 4]
    expected = -1
    assert find_first_unique(lst) == expected

    # Testcase 6: List with floating-point numbers
    lst = [1.5, 2.5, 3.5]
    expected = 1.5
    assert find_first_unique(lst) == expected

    print("\n\n💯💯All test cases passed!💯💯\n\n")


# Run the test cases
test_find_first_unique()
