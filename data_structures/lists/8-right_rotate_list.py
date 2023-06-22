def right_rotate(lst, k):
    """
    PROBLEM: Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.


    Input: A list and a positive number by which to rotate that list

    Output: The given list rotated by k elements

    Example Input: 
    lst = [10,20,30,40,50]
    k = 3

    Example Output:
    lst = [30,40,50,10,20]

    APPROACH:
    - Initial thoughts: Using kadane's algorithm, rotate all the elements before the index and all the elements after the index

    - Plan: 
        - To rotate from the K element, we need to make sure that the k element is within the list to avoid an IndexError exception. 
        - We need to make k the result of k mod len(lst). So that if K is larger than the length of the list, it would circle back to start from the beginning of the list.. See the illustration at the end of this file.
        - Next, we reverse the whole list and save it in a variable
        - Then we rotate the reversed list from the begining of the list untill k. We do this using slicing
        - Then we also use slicing to rotate the reversed list from k untill the end of the list.
        - Then we can add the left and right parts together
    """
    
    if lst == None:
        return 
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')

    if len(lst) == 0:
        k = 0
    else:
        # to make sure that k is within the bounds of the list
        k = k % len(lst)
    rotated_list = lst[::-1]
    left = rotated_list[:k][::-1]
    right = rotated_list[k:][::-1]

    return left+right


print(right_rotate(['right', 'rotate', 'python'], 4))
