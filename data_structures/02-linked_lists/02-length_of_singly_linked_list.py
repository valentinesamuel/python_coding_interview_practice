from DS_Classes.LinkedListClass import LinkedList as linked_list
import sys
sys.path.append('../DS_Classes/')

def length():
    """
    PROBLEM: In this problem, you have to implement the length() function which will find the length of a given linked list.

    Input: A linked list.

    Output: The number of nodes in the list.

    Example Input: 
    Linked List = 5->90->10->4  

    Example Output:
    4

    APPROACH:
    - Initial thoughts: Treat this like an array

    - Plan: 
        - if the head is None, that means the length is 0
        - Get the head node, while moving through the linked list, increment the length
        - after the the loop, increment the length by one again becasue the last node was the tail node that did not get checked because its next element was none
    """
    len = 0
    if linked_list.get_head():
        return len
    curr = linked_list.get_head()
    while curr.next_element:
        len+=1
        curr = curr.next_element
    len+=1
    return len