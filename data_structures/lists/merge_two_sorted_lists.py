def merge_lists(lst1, lst2):
    """
    PROBLEM: Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. 

    Input: Two sorted lists.

    Output: A merged and sorted list consisting of all elements of both input lists.

    Example Input: 
    list1 = [1,3,4,5]  
    list2 = [2,6,7,8]

    Example Output:
    arr = [1,2,3,4,5,6,7,8]

    APPROACH:
    - Initial thoughts: This problem can be solved using the merge part of the merge-sort algorithm.

    - Plan: 
        - Use two pointers, one at the beginning of each lists. Iterate through the array while the indices of each list is smallet than the length of the list.
        - At every iteration, check which one is bigger and smaller.
        - Put the smaller in the new list and move the pointer for that list foward. 
        - If any item is remaining in the list, just add it to the new list
        - Return the new list
    """

    if len(lst1) == 0 and len(lst2) == 0:
        return []
    if lst1 == None or lst2 == None:
        return
    if not isinstance(lst1, list) or not isinstance(lst2, list):
        raise TypeError('Invalid data type. Please input a list')

    idx1 = 0
    idx2 = 0
    arr = []
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] < lst2[idx2]:
            arr.append(lst1[idx1])
            idx1 += 1
        else:
            arr.append(lst2[idx2])
            idx2 += 1

    arr += lst1[idx1:]
    arr += lst2[idx2:]

    return arr


def test_merge_lists():
    # Test case 1: Normal input
    lst1, lst2 = [1, 3, 4, 5], [2, 6, 7, 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_lists(lst1, lst2) == expected

    # Test case 2: Empty list
    lst1, lst2 = [], []
    expected = []
    assert merge_lists(lst1, lst2) == expected

    # Test case 3: List with only even numbers
    lst1, lst2 = [], [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert merge_lists(lst1, lst2) == expected

    # Test case 3: An empty and unempty list
    lst1, lst2 = [1, 4, 45, 63], []
    expected = [1, 4, 45, 63]
    assert merge_lists(lst1, lst2) == expected

    print("All test cases passed!")


# Run the test cases
test_merge_lists()
