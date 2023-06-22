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


"""
                Explanation of k mod len(lst)
    Imagine you have a circular track with 10 positions labeled from 0 to 9. You have a toy car that you want to move along this track, and you have a number cube with numbers from 1 to 6 on its sides. Each time you roll the cube, it tells you how many positions you should move the car forward.

    Now, let's say you start with the car at position 0, and you roll the cube three times. The cube shows the numbers 4, 5, and 3. To determine the final position of the car, you can use the remainder pattern.

    Here's how it works:

    Start with the initial position of the car, which is 0.

    Roll the cube and get the first number, which is 4. Add this number to the current position: 0 + 4 = 4.

    Roll the cube again and get the second number, which is 5. Add this number to the current position: 4 + 5 = 9.

    Roll the cube one more time and get the third number, which is 3. Add this number to the current position: 9 + 3 = 12.

    Now, here's where the remainder pattern comes in. Since we are on a circular track with 10 positions, we can wrap around and start from the beginning if we go beyond position 9. To find the final position of the car, we take the remainder when the current position is divided by the total number of positions on the track.

    In this case, 12 divided by 10 gives a quotient of 1 and a remainder of 2. So, the final position of the car is 2.

    Using the remainder pattern, we ensure that the car stays within the valid range of positions on the track. It helps us achieve the circular rotation behavior we want.

    In the code we wrote above, the remainder pattern is used to ensure that the value of "k" (the number of positions to rotate) stays within the valid range of the list length. By taking the remainder of "k" divided by the length of the list, we make sure that "k" is always a non-negative number and less than the length of the list, which prevents any index out of range errors and allows for proper rotation.
"""
