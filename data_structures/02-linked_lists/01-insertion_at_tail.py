from DS_Classes.LinkedListClass import LinkedList as linked_list, Node
import sys
sys.path.append('../DS_Classes/')


def insert_at_tail(value):
    """
    PROBLEM: We need to insert a new object at the end of the linked list. You can naturally guess, that this newly added node will point to None as it is at the tail.

    Input: A linked list and an integer value.

    Output: The updated linked list with the value inserted.

    Example Input: 
    Linked List = 0->1->2
    integer = 3

    Example Output:
    Linked List = 0->1->2->3

    APPROACH:
    - Initial thoughts: We shold look for a way to add the node at the first place without losing pointers

    - Plan: 
        - check if the linked list is empty. If it is, assign the node to the be the head node of the linked list
        - if the list is not empty, get the head pointer of the list and iterate till the current node's pointer is None.
        - On every iteration, assign the next element of the current node to the current node
    """
    new_node = Node(value)
    if linked_list.get_head() is None:
        linked_list.head_node = new_node
        return
    current = linked_list.get_head()
    while current.next_element is not None:
        current = current.next_element
    current.next_element = new_node
    return
