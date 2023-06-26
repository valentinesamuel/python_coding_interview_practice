def find_product(lst):
    """
    PROBLEM: Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

    Input: A list of numbers (could be floating points or integers)

    Output: A list such that each index has a product of all the numbers in the list except the number stored at that index.

    Example Input: 
    arr1 = [1,2,3,4]
    arr2 = [2, 5, 9, 3, 6]
    arr3 = [0, 1, 10, 100]
    arr4 = [0, 2, 9, 0, 12, 25]

    Example Output:
    arr1 = [24,12,8,6]
    arr2 = [810, 324, 180, 540, 270]
    arr3 = [1000, 0, 0, 0]
    arr4 = [0, 0, 0, 0, 0, 0]

    APPROACH:
    - Initial thoughts: Find the product of the whole array and at each index, divide the total product by the index value. But some platforms do not allow this.

    - Plan: 
        - Iterate through the array
        - Create a new array that would hold the product of all values to the left of the indexed value.
        - Since there is no element before the fist element, initialize the left variable to 1 and append it to the array and move to the next index
            - Then we update the left variable to be the product of the left variable and the number at the current index. Else, we will have 1s through out the array.
        - Then we start at the last index of the input array and multiply the left product value and the right product.
            - Then we update the right product value to hold the product of the right value and the value at the current index from the inout array
    """

    if len(lst) == 0:
        return lst
    if lst == None:
        return 
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')

    prod = []
    left = 1
    for num in lst:
        prod.append(left)
        left*=num
    right = 1
    for idx in range(len(lst)-1, -1, -1):
        prod[idx] = prod[idx] * right
        right *= lst[idx]  

    return prod

def test_find_product():
    # Testcase 1: Normal input
    lst = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert find_product(lst) == expected

    # Testcase 2: Empty list
    lst = []
    expected = []
    assert find_product(lst) == expected

    # Testcase 3: List with one element
    lst = [5]
    expected = [1]
    assert find_product(lst) == expected

    # Testcase 4: List with zeros
    lst = [0, 2, 9, 0, 12, 25]
    expected = [0, 0, 0, 0, 0, 0]
    assert find_product(lst) == expected

    print("\n\n💯💯All test cases passed!💯💯\n\n")

# Run the test cases
test_find_product()