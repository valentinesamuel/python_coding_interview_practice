from DS_Classes.LinkedListClass import LinkedList
import sys
sys.path.append('../DS_Classes/')


def remove_duplicates(lst: LinkedList) -> LinkedList:
    """
    PROBLEM: You will now be implementing the remove_duplicates() function. When a linked list is passed to this function, it removes any node which is a duplicate of another existing node.

    Input: A linked list with duplicate nodes.

    Output: A linked list without duplicate values

    Example Input: 
    LinkedList = 1->2->2->2->3->4->4->5->6

    Example Output:
    LinkedList = 1->2->3->4->5->6

    APPROACH:
    - Initial thoughts: we can use a hashmap for this and store the frequency of the node in a hashmap. Then traverse through the hashmap again and reorder the node pointer

    - Plan: 
        - check if the linked list is empty 
        - while there is still a node, if the node value is in the hashmap, then we point the previous node to the next node after the current node
        - if it does not exist, we add the node value as key in the hashmap and move the follower then the pointer.
    """
    if not lst.get_head():
        return
    register = {}
    curr = lst.get_head()
    follower = lst.get_head()

    while curr:
        if not curr.data in register:
            register[curr.data] = 1
            follower = curr
            curr = curr.next_element
        else:
            follower.next_element = curr.next_element
            curr = curr.next_element
    return lst
