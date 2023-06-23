def max_min(lst):
    """
    PROBLEM: Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.

    Input: A sorted list

    Output: A list with elements stored in max/min form

    Example Input: 
    lst = [1,2,3,4,5]

    Example Output:
    lst = [5,1,4,2,3]

    APPROACH:
    - Initial thoughts: We can use two pointers for this

    - Plan: 
        - We put one pointer at the beginning of the list and the other one at the end
        - While the left pointer is less than or equal to the right pointer
            If the left pointer is the right pointer, then we append to the list using the left pointer.
            - Else we add the right then the left pointer.
            - As we move through the list, we add the right and then the left item in to the resulting array
            - Then we move the left pointer foward and the right pointer backward.
    """


    if lst == None:
        return
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')
    # If the list has exactly two elements and the first element is greater than the second
    if len(lst) == 2 and lst[0] > lst[1]:  
        return lst 
        
    left = 0
    right = len(lst) - 1
    res = []
    while left <= right:
        if left == right:
            res.append(lst[left])
        else:
            res.append(lst[right])
            res.append(lst[left])
        left+=1
        right-=1
    return res

def test_max_min():
    # Testcase 1: Normal input with an even-length list
    lst = [1, 2, 3, 4, 5, 6]
    expected = [6, 1, 5, 2, 4, 3]
    assert max_min(lst) == expected

    # Testcase 2: Normal input with an odd-length list
    lst = [1, 2, 3, 4, 5]
    expected = [5, 1, 4, 2, 3]
    assert max_min(lst) == expected

    # Testcase 3: Empty list
    lst = []
    expected = []
    assert max_min(lst) == expected

    # Testcase 4: List with a single element
    lst = [10]
    expected = [10]
    assert max_min(lst) == expected

    # Testcase 5: List with two elements
    lst = [8, 3]
    expected = [8, 3]
    assert max_min(lst) == expected

    print("\n\n💯💯All test cases passed!💯💯\n\n")

test_max_min()