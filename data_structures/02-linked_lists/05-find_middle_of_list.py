from DS_Classes.LinkedListClass import LinkedList
import sys
sys.path.append('../DS_Classes/')


def find_mid(lst: LinkedList):
    """
    PROBLEM: You have to implement the find_mid() function which will take a linked list as an input and return the value of the middle node. If the length of the list is even, the middle value will occur at len(lst) / 2. For a list of odd length, the middle value will be len(lst)/2 + 1.

    Input: A singly linked list .

    Output: An integer value of the middle node

    Example Input: 
    LinkedList = 7->14->10->21

    Example Output:
    LinkedList = 14

    APPROACH:
    - Initial thoughts: Since we were given the hint in the problem stateent. We need to get the length of the list

    - Plan: 
        - check if the linked list is empty 
        - get the length of the list and check it its even or not and apply the formula accordingly. The result is where we are goint to stop traversal
        - while an iterator that starts from one is less than the result, we keep on moving. When we get there, we return the data of that node
    """

    if not lst.get_head():
        return
    trav = 0
    length = lst.length()
    if length % 2 == 0:
        trav = length // 2
    else:
        trav = (length // 2) + 1
    i = 1
    curr = lst.get_head()
    while i < trav:
        curr = curr.next_element
        i += 1
    return curr.data
