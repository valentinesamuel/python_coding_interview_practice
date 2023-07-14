from DS_Classes.LinkedListClass import LinkedList as linked_list, Node
import sys
sys.path.append('../DS_Classes/')


def search(value: Node) -> bool:
    """
    PROBLEM: To search for a specific value in a linked list, there is no other approach but to traverse the whole list until we find the desired value. In that sense, the search operation in linked lists is similar to the linear search in normal lists or arrays - all of them take O(n) amount of time.

    Input: A linked list and an integer to be searched.

    Output: True if the integer is found. False otherwise.

    Example Input: 
    Linked List = 5->90->10->4  
    Integer = 4

    Example Output:
    True

    APPROACH:
    - Initial thoughts: Since we have to look at every node. When we get to each node, we should check if the value we are looking for is in that node's data store

    - Plan: 
        - On every node, check if the node that we are looking for is the node that is that data store
        - If it is, then we return true else we return false.
        - An edge case is to check the last node before we return false since we did not check it in the loop because the last node's next_element points to null
    """

    if linked_list.get_head() == None:
        return False
    current = linked_list.get_head()
    while current.next_element:
        if current.data == value:
            return True
        current = current.next_element
    if current.data == value:
        return True
    return False
