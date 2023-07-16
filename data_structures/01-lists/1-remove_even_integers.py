def remove_even(lst: list) -> list:
    """
    PROBLEM: Implement a function that removes all the even elements from a given list.

    Input: A list with random integers.

    Output: A list with only odd integers

    Example Input: 
    my_list = [1,2,4,5,10,6,3]  

    Example Output:
    my_list = [1,5,3]

    APPROACH:
    - Initial thoughts: This problem can be solved using the modulo operator, which is an efficient way to find out if there is a remainder after dividing a number.
    
    - Plan: 
        - Iterate through the array, check the remainder of the current number using number % 2. 
        - If the remainder is not 0, then that number is an odd number because 2 is an even number and it can divide any even number without remainder
    """


    if len(lst) == 0:
        return lst
    if lst == None:
        return 
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')

    result = []
    for idx in range(len(lst)):
        if lst[idx] % 2 != 0:
            result.append(lst[idx])
    return(result)


def test_remove_even():
    # Test case 1: Normal input
    lst = [20, 36, -139, 12, -31, 168, -66, -36, 151, -132, 30, -17, -179, 133, -91, 61, -112, 23, 77, 53, -64, 81, 191, 8, -40, 163, -107, 29, -56, -121, -63, 45]
    expected = [-139, -31, 151, -17, -179, 133, -91, 61, 23, 77, 53, 81, 191, 163, -107, 29, -121, -63, 45]
    assert remove_even(lst) == expected

    # Test case 2: Empty list
    lst = []
    expected = []
    assert remove_even(lst) == expected

    # Test case 3: List with only even numbers
    lst = [2, 4, 6, 8, 10]
    expected = []
    assert remove_even(lst) == expected

    # Test case 4: List with only odd numbers
    lst = [1, 3, 5, 7, 9]
    expected = [1, 3, 5, 7, 9]
    assert remove_even(lst) == expected

    # Test case 5: List with a single even number
    lst = [2]
    expected = []
    assert remove_even(lst) == expected

    # Test case 6: List with a single odd number
    lst = [3]
    expected = [3]
    assert remove_even(lst) == expected

    # Test case 7: List with a mix of even and odd numbers
    lst = [2, 5, 4, 7, 6, 9, 8]
    expected = [5, 7, 9]
    assert remove_even(lst) == expected

    print("\n\n💯💯All test cases passed!💯💯\n\n")
# Run the test cases
test_remove_even()